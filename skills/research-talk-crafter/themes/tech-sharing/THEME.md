# Tech Sharing

Source: https://open-design.ai/plugins/example-html-ppt-tech-sharing/  
Author: lewislulu (html-ppt-skill, MIT); amber restyle by OpenDesign (Apache-2.0)  
Licence: MIT + Apache-2.0 (LICENSE files in this folder)

## Files
- `example.html`: the seed deck, verbatim from the template.
- `layouts.html`: research slides (figure, robot video, equation, results table) built from this theme's own classes, tokens and px sizes.
- `UPSTREAM-SKILL.md`: the template author's own rules (locked design).

## Stance
Amber-phosphor terminal deck: warm off-black, one CRT-amber accent, IBM Plex Mono structure, hairline panels, sharp corners, no gradients or shadows.

## Canvas
Fluid: each slide is 100vw x 100vh, padding 72px 96px; static preview (slides stacked, no runtime). Upstream runtime adds keyboard nav, S presenter popup, N notes, O overview.

## Fonts (exact)
- **Sora** 500 600 700: display (h1, h2, h4, agenda titles)
- **IBM Plex Sans** 400 500 700: body
- **IBM Plex Mono** 400 500 600, italic 400: kickers, terminal, tags, footer

## Type scale as shipped (keep every size)

| Role | Family | Weight | px | ≈pt on 16:9 | Notes |
|---|---|---|---|---|---|
| h1 title | Sora | 700 | 76 | 38 | line-height 1.06, tracking -0.02em |
| h2 title | Sora | 600 | 50 | 25 | line-height 1.14, tracking -0.015em |
| h3 | IBM Plex Sans | 600 | 30 | 15 | line-height 1.25 |
| agenda row title | Sora | 600 | 23 | 11.5 | tracking -0.01em |
| lede | IBM Plex Sans | 400 | 21 | 10.5 | line-height 1.6, max 62ch, text-2 |
| h4 card title | Sora | 600 | 20 | 10 | line-height 1.35 |
| card body | IBM Plex Sans | 400 | 15.5 | 7.75 | line-height 1.7 |
| terminal code | IBM Plex Mono | 400 | 15 | 7.5 | line-height 1.7 |
| kicker | IBM Plex Mono | 500 | 13 | 6.5 | accent, prefixed with '> ' |
| tag | IBM Plex Mono | 400 | 12.5 | 6.25 | hairline outline |
| footer / page no. | IBM Plex Mono | 400 | 12 | 6 | text-3 |

Other px values that appear in `example.html` (inline overrides, captions) are also part of the shipped scale; `scripts/lint_deck.py` reads them from there.

## Colour tokens (exact)

| Token | Value | Role |
|---|---|---|
| `--bg` | `#151210` | slide background |
| `--surface` | `#1c1814` | terminal title bar, avatar |
| `--text-1` | `#ece7df` | primary text |
| `--text-2` | `#a89f91` | lede, card body |
| `--text-3` | `#8d8476` | captions, footer |
| `--accent` | `#e8973c` | CRT amber: kickers, highlights, one tick per slide |
| `--accent-deep` | `#a85d14` | hot-card border, accent on paper |
| `--paper` | `#f1ece3` | the single inverted closing slide |
| `--paper-ink` | `#1c1814` | text on paper |
| `--line` | `rgba(236,231,223,.14)` | hairlines |

## Signature devices (every deck must show them)
- Terminal gutter: 1px vertical hairline at left:56px with a 9px amber tick at top:72px on every slide
- Mono kicker with '> ' prefix above each title (e.g. 'agenda.toml', '// why-now')
- Hairline cards, radius 0, no shadow; one 'hot' card per row with amber top border and 5% amber fill
- Terminal window: 9px dots (first one amber), file name in the bar, warm syntax (kw amber, str sand, cmt dim italic)
- Agenda rows: mono number, Sora title, mono duration on the right, hairline rules
- One deliberate inversion: closing slide on paper with a large '>_' glyph

## Layouts
Seed: cover with speaker block, agenda rows, 3-card context row, text + terminal split, text + checklist card, full-width code, 3 takeaway cards, inverted Q&A close.
Research (layouts.html): figure with caption, robot video with on-frame tags, equation with colour-linked terms, three-rule results table.

## Motion
kf-rise: opacity 0 + translateY(24px) to rest, 0.6-0.7s cubic-bezier(.16,1,.3,1); kicker, then title (+0.06s), then body (+0.14s). Reduced motion: none.

## For research talks
Good for systems / robotics-software talks and code walkthroughs. Gaps: no figure or plot layout, no maths, dark background for papers' white figures. Body text is web-sized (see flags).

## Flags (information only; sizes stay as shipped)
- Card body 15.5px, terminal 15px, kicker 13px, tags and footer 12-12.5px, and lede 21px (10.5pt) are small for large rooms.
- Dark background: paper figures with white backgrounds need re-export with transparent backgrounds.

## Demo content to delete
The seed's demo content must not survive into a real deck. Lint looks for: `OpenDesign`, `Staff Developer-Advocate`, `agent-stream`, `Platform DevEx`, `devrel`.

## How to use
1. Start from `example.html` and `layouts.html`. Replace content only.
2. Keep the `:root` tokens, font families and weights, every px size, letter-spacing, the devices and the script exactly as shipped.
3. Never substitute fonts or add colours outside the token table.
4. A slide type the theme lacks is composed from its existing classes and tokens.
5. For other output formats, see `../../references/porting.md`.
