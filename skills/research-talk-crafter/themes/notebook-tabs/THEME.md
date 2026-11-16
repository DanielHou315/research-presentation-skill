# Notebook Tabs

Source: https://open-design.ai/plugins/example-fs-notebook-tabs/  
Author: Zara Zhang (frontend-slides, MIT)  
Licence: MIT (LICENSE files in this folder)

## Files
- `example.html`: the seed deck, verbatim from the template.
- `layouts.html`: research slides (figure, robot video, equation, results table) built from this theme's own classes, tokens and px sizes.
- `UPSTREAM-SKILL.md`: the template author's own rules (locked design).

## Stance
A physical notebook: cream paper card on a dark desk, binder holes, pink margin rule, five pastel index tabs on the fore-edge marking the current section.

## Canvas
Fixed 1920x1080 .deck-stage scaled uniformly; paper inset 56/150/56/120px; content padding 78px 110px (150px left).

## Fonts (exact)
- **Bodoni Moda** 400 700, italic 400: display, headings, numerals, quotes
- **DM Sans** 400 500 700: body, labels, tabs, chrome

## Type scale as shipped (keep every size)

| Role | Family | Weight | px | ≈pt on 16:9 | Notes |
|---|---|---|---|---|---|
| section numeral (outlined) | Bodoni Moda | 400 | 430 | 215 | line-height 0.85, 2px stroke, transparent fill |
| big stat | Bodoni Moda | 700 | 300 | 150 | unit below in 120px italic |
| quote mark | Bodoni Moda | 400 | 220 | 110 | lavender |
| display title | Bodoni Moda | 700 | 150 | 75 | line-height 0.98; one italic 400 word |
| h2 | Bodoni Moda | 700 | 84 | 42 | line-height 1.04; 58-64px on dense slides |
| quote | Bodoni Moda italic | 400 | 66 | 33 | line-height 1.25 |
| contents title | Bodoni Moda | 400 | 40 | 20 |  |
| point / card heading | Bodoni Moda | 700 | 36 | 18 | 32-40px |
| cover edition line | Bodoni Moda italic | 400 | 34 | 17 |  |
| subtitle / lede | DM Sans | 400 | 30 | 15 | line-height 1.5, max 980px |
| body | DM Sans | 400 | 26 | 13 | line-height 1.5; list items 25px, card body 23px |
| bar label / links | DM Sans | 400 | 20 | 10 | uppercase, tracking 0.1-0.2em |
| label / kicker / tabs | DM Sans | 700 | 17 | 8.5 | uppercase, tracking 0.26-0.3em |
| baseline footer | DM Sans | 400 | 15 | 7.5 | uppercase, tracking 0.24em |

Other px values that appear in `example.html` (inline overrides, captions) are also part of the shipped scale; `scripts/lint_deck.py` reads them from there.

## Colour tokens (exact)

| Token | Value | Role |
|---|---|---|
| `--bg-outer` | `#2d2d2d` | dark desk behind the paper |
| `--bg-page` | `#f8f6f1` | cream paper |
| `--text-primary` | `#1a1a1a` | primary text |
| `--text-secondary` | `#6b6358` | labels, lede, body |
| `--rule` | `#d8d2c4` | hairlines, dotted leaders |
| `--tab-1` | `#98d4bb` | mint tab (section 1) |
| `--tab-2` | `#c7b8ea` | lavender tab |
| `--tab-3` | `#f4b8c5` | pink tab, margin rule |
| `--tab-4` | `#a8d8ea` | sky tab, 'hot' column shadow |
| `--tab-5` | `#ffe6a7` | cream tab |

## Signature devices (every deck must show them)
- Paper card with layered drop shadow and faint 44px ruled grain
- Ten punched binder holes down the left margin; 1px pink margin rule at 92px
- Five vertical index tabs on the right edge, tucked under the paper; current section's tab is pulled out
- Running head 'No. NN' + section, and a baseline 'section / NN of total', both hairline-ruled
- Outlined 430px Bodoni section numeral
- Colour chips that tie kickers, contents rows and bars to their section's tab colour
- Hard 8px offset shadow in sky blue on the 'this work' comparison column

## Layouts
Seed: cover, contents with dotted leaders, section divider, 3 pinned points, quote, big stat + side note, CSS bar chart, two-column comparison, 2x2 contribution grid, closing with limitations.
Research (layouts.html): figure with caption, robot video with on-frame tags, equation with colour-linked terms, three-rule results table.

## Motion
Reveal: translateY(28px) + fade, 0.7s cubic-bezier(.16,1,.3,1), staggered 0.1s; bars grow with scaleY 0.9s. Reduced motion: fades only.

## For research talks
Built for capstone and thesis defenses; the tab index works as a live agenda. Largest body text of the five. Gaps: playful tone for a conference, no figure-image, video or maths layout, max 3 points per slide.

## Flags (information only; sizes stay as shipped)
- Footer 15px and labels/tabs 17px are below 24px (12pt); body 26px (13pt) and lede 30px (15pt) pass the Slides floor but are under the 18-24pt that talk advice asks for.
- Max 3 points per slide is a template rule.

## Demo content to delete
The seed's demo content must not survive into a real deck. Lint looks for: `TypeAhead`, `Jordan Ames`, `Elena Cho`, `Gboard`, `SwiftKey`.

## How to use
1. Start from `example.html` and `layouts.html`. Replace content only.
2. Keep the `:root` tokens, font families and weights, every px size, letter-spacing, the devices and the script exactly as shipped.
3. Never substitute fonts or add colours outside the token table.
4. A slide type the theme lacks is composed from its existing classes and tokens.
5. For other output formats, see `../../references/porting.md`.
