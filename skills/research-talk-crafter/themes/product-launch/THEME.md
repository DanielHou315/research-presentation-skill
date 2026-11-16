# Product Launch

Source: https://open-design.ai/plugins/example-html-ppt-product-launch/  
Author: lewislulu (html-ppt-skill, MIT); editorial restyle by OpenDesign (Apache-2.0)  
Licence: MIT + Apache-2.0 (LICENSE files in this folder)

## Files
- `example.html`: the seed deck, verbatim from the template.
- `layouts.html`: research slides (figure, robot video, equation, results table) built from this theme's own classes, tokens and px sizes.
- `UPSTREAM-SKILL.md`: the template author's own rules (locked design).

## Stance
Warm editorial launch keynote: one burnt-orange accent, warm off-white paper, warm off-black ink, Fraunces variable serif with optical sizing, hairline ledgers.

## Canvas
Fluid: 100vw x 100vh slides, padding 88px 104px; headline sizes use clamp() against viewport width; static preview.

## Fonts (exact)
- **Fraunces** 400-600 variable, opsz 9-144, italic: display, numerals, quotes
- **Outfit** 300 400 500 600: body
- **JetBrains Mono** 400 500: kickers, footer, units

## Type scale as shipped (keep every size)

| Role | Family | Weight | px | ≈pt on 16:9 | Notes |
|---|---|---|---|---|---|
| intro nameplate h1 | Fraunces | 560 opsz 110 | 168 | 84 | clamp(110px,12.5vw,168px), line-height 1 |
| h1 | Fraunces | 560 opsz 110 | 104 | 52 | clamp(64px,7.6vw,104px), line-height 1.02, tracking -0.018em |
| closing big number | Fraunces | 560 opsz 110 | 118 | 59 | clamp(80px,8vw,118px), accent-bright |
| price amount | Fraunces | 560 opsz 90 | 76 | 38 | clamp(54px,5.4vw,76px), tracking -0.025em |
| h2 | Fraunces | 540 opsz 90 | 62 | 31 | clamp(42px,4.8vw,62px), line-height 1.06 |
| column stat | Fraunces | 540 opsz 80 | 54 | 27 | clamp(40px,3.8vw,54px) |
| pull quote | Fraunces italic | 480 opsz 80 | 42 | 21 | clamp(30px,3.3vw,42px), max 26ch |
| step numeral | Fraunces italic | 500 opsz 60 | 38 | 19 | accent |
| lede | Outfit | 300 | 20 | 10 | line-height 1.55, max 56ch, ink-2 |
| h4 | Outfit | 600 | 20 | 10 | tracking -0.01em |
| body (dim) | Outfit | 400 | 15.5 | 7.75 | line-height 1.6, max 44ch |
| kicker | JetBrains Mono | 500 | 12 | 6 | uppercase, tracking 0.15em, accent |
| footer | JetBrains Mono | 400 | 11.5 | 5.75 | tracking 0.04em, ink-3 |

Other px values that appear in `example.html` (inline overrides, captions) are also part of the shipped scale; `scripts/lint_deck.py` reads them from there.

## Colour tokens (exact)

| Token | Value | Role |
|---|---|---|
| `--paper` | `#f7f3ec` | slide background |
| `--paper-2` | `#efe9df` | secondary paper |
| `--ink` | `#191511` | primary text; background of the one inverted slide |
| `--ink-2` | `#544c44` | lede, body |
| `--ink-3` | `#6e6459` | footer, labels |
| `--accent` | `#a63e0c` | burnt orange: kicker, rule, italic emphasis, proposed column |
| `--accent-bright` | `#d9651f` | accent on ink |
| `--line` | `rgba(25,21,17,.13)` | hairlines |

## Signature devices (every deck must show them)
- Cover anchored to the bottom: mono kicker, 72x3px accent rule, three-line serif headline whose last line is italic accent
- Centred nameplate slide framed by two strong hairlines
- Hairline column grids (3-up / 2-up) with a glyph or serif stat on top of each column
- Ledger rows with italic serif step numerals in accent
- Pricing ledger: three columns, proposed column gets a 3px accent top bar
- One inverted ink slide for the close: italic pull quote + huge accent number + button
- Mono footer baseline: audience on the left, 'n / total' on the right

## Layouts
Seed: bottom-anchored cover, centred nameplate, 3-column pillars, 3-column stats, 2-column proof, 4-step ledger, 3-plan pricing ledger, inverted quote + CTA.
Research (layouts.html): figure with caption, robot video with on-frame tags, equation with colour-linked terms, three-rule results table.

## Motion
rise: translateY(24px) + fade, 0.7s cubic-bezier(.16,1,.3,1), children staggered 0.06s.

## For research talks
Best match for job talks, invited talks and openings where the narrative matters. Gaps: no figure, video or maths layout; body text web-sized.

## Flags (information only; sizes stay as shipped)
- Body 15.5px, kicker 12px, footer 11.5px and lede 20px are small for large rooms.
- Headline sizes use clamp() on viewport width, so they shrink in small windows; when porting to a fixed canvas, use the 1920px value (the clamp maximum).

## Demo content to delete
The seed's demo content must not survive into a real deck. Lint looks for: `OpenDesign`, `Northwind`, `Priya Shah`, `Marcus Webb`, `open-design.ai`.

## How to use
1. Start from `example.html` and `layouts.html`. Replace content only.
2. Keep the `:root` tokens, font families and weights, every px size, letter-spacing, the devices and the script exactly as shipped.
3. Never substitute fonts or add colours outside the token table.
4. A slide type the theme lacks is composed from its existing classes and tokens.
5. For other output formats, see `../../references/porting.md`.
