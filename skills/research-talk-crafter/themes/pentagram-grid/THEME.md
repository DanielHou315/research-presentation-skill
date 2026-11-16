# Pentagram Grid

Source: https://open-design.ai/plugins/example-huashu-pentagram-grid/  
Author: alchaincyf / huashu-design ppt-pentagram (MIT), extended to a deck by OpenDesign  
Licence: MIT (+ Apache-2.0 for OpenDesign changes) (LICENSE files in this folder)

## Files
- `example.html`: the seed deck, verbatim from the template.
- `layouts.html`: research slides (figure, robot video, equation, results table) built from this theme's own classes, tokens and px sizes.
- `UPSTREAM-SKILL.md`: the template author's own rules (locked design).

## Stance
Swiss info-architecture: white paper with black bookends, one red (#E63946) exactly where the eye must land, giant weight-900 numerals, measured grid.

## Canvas
Fixed 1920x1080 #stage scaled by fit(); every measurement in px; 80px outer margins; 64px chrome bars.

## Fonts (exact)
- **Helvetica Neue (system stack)** 400 500 600 700 900: the only family; no web fonts; falls back to Arial on Windows

## Type scale as shipped (keep every size)

| Role | Family | Weight | px | ≈pt on 16:9 | Notes |
|---|---|---|---|---|---|
| hero numeral | Helvetica Neue | 900 | 260 | 130 | line-height 0.85, tracking -13px; red decimal/unit |
| divider chapter number | Helvetica Neue | 900 | 260 | 130 | fully red on dark pages |
| stats-grid numeral | Helvetica Neue | 900 | 128 | 64 | tracking -6px |
| cover / closing headline | Helvetica Neue | 900 | 120 | 60 | tracking -5px, red full stop |
| timeline numeral | Helvetica Neue | 900 | 96 | 48 | graded grey to black to red |
| divider title | Helvetica Neue | 900 | 84 | 42 | tracking -3px |
| bench hero | Helvetica Neue | 900 | 80 | 40 | tracking -3px |
| contents headline | Helvetica Neue | 900 | 72 | 36 | tracking -3px |
| section headline | Helvetica Neue | 900 | 64 | 32 | tracking -2px |
| quote | Helvetica Neue | 900 | 54 | 27 | line-height 1.4, key phrase red |
| summary number | Helvetica Neue | 900 | 32 | 16 | tracking -1px |
| contents row | Helvetica Neue | 700 | 28 | 14 |  |
| body / key message | Helvetica Neue | 400 | 17 | 8.5 | 15-18px, line-height 1.7, #666 |
| bar value | Helvetica Neue | 700 | 15 | 7.5 | inside the bar |
| bar label / kicker | Helvetica Neue | 600-900 | 13 | 6.5 |  |
| labels / chrome | Helvetica Neue | 700 | 11 | 5.5 | 11-12px uppercase, tracking 2-3px |

Other px values that appear in `example.html` (inline overrides, captions) are also part of the shipped scale; `scripts/lint_deck.py` reads them from there.

## Colour tokens (exact)

| Token | Value | Role |
|---|---|---|
| `--paper` | `#FFFFFF` | light pages |
| `--night` | `#111111` | dark pages, 64px chrome bars |
| `--ink` | `#111111` | text on light |
| `--accent` | `#E63946` | the only red; at most 4 touches per page |
| `--grid` | `#E8E8E8` | hairlines |
| `--track` | `#F5F5F5` | bar track |
| `--bar-base` | `#E0E0E0` | losing / baseline bar |
| `--muted` | `#999999` | labels |
| `--muted-2` | `#666666` | body copy |
| `--faint` | `#BBBBBB` | tertiary captions |
| `--night-line` | `#333333` | hairlines on dark |
| `--night-mut` | `#888888` | secondary text on dark |

## Signature devices (every deck must show them)
- 64px black chrome bars top and bottom: uppercase label with a red '/', red right label, 900-weight logotype + divider + footnote
- Swiss grid hairlines: 1px verticals and horizontals at 5% opacity on the 80px gutters
- One giant 900-weight numeral per hero page; only its decimal point, slash or unit is red
- Red / black / grey bar charts: the subject is always the red bar, value printed inside
- Summary strip: hairline-topped row of 32px numbers with uppercase captions
- Outlined red badge, square corners; zero border-radius everywhere
- White pages dominate; at most 2-3 dark pages (divider, closing)

## Layouts
Seed: cover (statement + hero numeral), contents rows, big-number + stat rail, data-theater (3 bar-chart columns + summary), dark divider, before/after bars, timeline, quote, 2x2 stats grid, dark closing.
Research (layouts.html): figure with caption, robot video with on-frame tags, equation with colour-linked terms, three-rule results table.

## Motion
Opacity-only page fade 0.45s cubic-bezier(.16,1,.3,1); nothing else moves.

## For research talks
Strongest for results-heavy talks: the red-bar convention maps directly to 'ours vs baselines'. Gaps: body and labels are very small for projection, Helvetica Neue isn't free to ship, no figure-image or maths layout.

## Flags (information only; sizes stay as shipped)
- Body 15-18px and labels 11-13px sit on a fixed 1920 canvas, so they project at 5.5-9pt, well below the 18-24pt talk advice asks for.
- Contrast: --muted #999 on white is 2.85:1 and --faint #BBB is 1.92:1 (both fail 4.5:1); small red text #E63946 on white is 4.17:1 (fails below large-text size; the seed uses red mostly on large numerals and bars).
- Helvetica Neue is a licensed system font, not shipped; on Windows/Linux it falls back to Arial.

## Demo content to delete
The seed's demo content must not survive into a real deck. Lint looks for: `OPENDESIGN`, `OpenDesign`, `Positioning`, `析衡`, `XIHENG`.

## How to use
1. Start from `example.html` and `layouts.html`. Replace content only.
2. Keep the `:root` tokens, font families and weights, every px size, letter-spacing, the devices and the script exactly as shipped.
3. Never substitute fonts or add colours outside the token table.
4. A slide type the theme lacks is composed from its existing classes and tokens.
5. For other output formats, see `../../references/porting.md`.
