# Porting a theme to another output format

The themes ship as HTML. When your harness produces something else (a .pptx file, Claude Slides,
Codex slides, Google Slides, Keynote, Beamer), reproduce the theme from `themes/<id>/THEME.md` and
`themes/specs.json`. Don't eyeball the HTML.

## What must stay exact

| Property | Rule |
|---|---|
| Font families and weights | The ones in THEME.md. Load web fonts where the format allows; for .pptx, embed the fonts or tell the user to install them (all except Helvetica Neue are free Google Fonts). |
| Sizes | Every px size as shipped. On a 1920×1080 slide, 1 px = 0.5 pt (13.33 × 7.5 in). Fluid themes (Product Launch, Tech Sharing, Cyber Terminal) size against a 1920×1080 window. |
| Colours | The token values exactly, in the roles THEME.md gives them. No new colours. |
| Tracking and line height | As listed. |
| Signature devices | All of them, on every slide where the seed shows them. |
| Light/dark rhythm | Same as the seed (for example Pentagram: white pages, at most 2–3 dark pages). |

## If your format sets a minimum size

Some formats refuse small text (Claude Slides renders nothing under 24px). Raise only the roles the
format forces up, to its minimum and no further, leave everything else as shipped, and list the
roles you changed for the user.

## Rebuilding devices a format can't express

| Device (theme) | HTML technique | Substitute |
|---|---|---|
| Terminal gutter hairline + amber tick (Tech Sharing) | `::before` / `::after` | A 1px line shape at x=56px and a 9×1px accent shape at y=72px on the master |
| Window chrome dots + shell path (Cyber Terminal) | flex row | Three 11px circles + a mono text box on the master |
| Scanlines, masked grid, vignette (Cyber Terminal) | repeating gradients, mask, blend modes | A pre-rendered transparent PNG overlay on the master, or drop and say so |
| Glow on titles (Cyber Terminal) | text-shadow | Outer glow in .pptx; drop where unsupported |
| 64px black chrome bars (Pentagram) | absolutely positioned divs | Full-width rectangles on the master |
| Grid hairlines at 5% opacity (Pentagram) | 1px divs | 1px lines, black at 5% transparency |
| Paper card, binder holes, margin rule (Notebook Tabs) | layered shadows, gradients | Rounded rectangle with soft shadow, 10 circles, 1px pink line on the master |
| Vertical index tabs (Notebook Tabs) | `writing-mode: vertical-rl` | Rotated text boxes on coloured shapes; the active tab offset 6px |
| Outlined section numeral (Notebook Tabs) | `-webkit-text-stroke` | Text outline with no fill (.pptx), or an SVG |
| Optical-size Fraunces (Product Launch) | `font-variation-settings` | The nearest static instance (Fraunces 72pt or 144pt cut) |
| Hairline ledgers and column rules (Product Launch, Tech Sharing) | borders | 1px lines at the token colour and opacity |

## Tell the user

When you hand over a ported deck, list every device you substituted or dropped and every size you
raised, and say why (the format's limit).

## Format notes

- **.pptx.** Build a slide master per theme with named layouts matching the seed's layouts plus the
  research layouts. Set theme colours with the accent in `accent1`, so native charts inherit "ours"
  = accent. Use real placeholders (title, body, picture, media) so content can be dropped in.
- **Slide tools without scripts (Claude Slides and similar).** Navigation scripts are dropped:
  the tool navigates. Use the tool's click steps for builds. Equations become MathML or SVG
  images (`scripts/render_math.mjs`).
- **Beamer.** Set the families with fontspec (XeLaTeX or LuaLaTeX), define the token colours with
  xcolor, and draw devices in the background template with TikZ.
