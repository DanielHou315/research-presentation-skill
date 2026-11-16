# Cyber Terminal (hermes)

Source: https://open-design.ai/plugins/example-html-ppt-hermes-cyber-terminal/  
Author: lewislulu (html-ppt-skill, MIT); repointed tokens by OpenDesign (Apache-2.0)  
Licence: MIT + Apache-2.0 (LICENSE files in this folder)

## Files
- `example.html`: the seed deck, verbatim from the template.
- `layouts.html`: research slides (figure, robot video, equation, results table) built from this theme's own classes, tokens and px sizes.
- `UPSTREAM-SKILL.md`: the template author's own rules (locked design).

## Stance
Dark terminal with neon mint/cyan, scanlines, masked grid and vignette; everything reads like a live shell session.

## Canvas
Fluid: 100vw x 100vh slides, padding 60px 84px; static preview; upstream runtime has presenter view and notes.

## Fonts (exact)
- **JetBrains Mono** 400 500 700: display, headings, labels, code (the deck's voice)
- **Geist** 300 400 500: lede and card descriptions

## Type scale as shipped (keep every size)

| Role | Family | Weight | px | ≈pt on 16:9 | Notes |
|---|---|---|---|---|---|
| big stat | JetBrains Mono | 700 | 140 | 70 | tracking -0.04em, mint glow |
| cover / divider h1 | JetBrains Mono | 700 | 110 | 55 | 96-120px inline overrides, mint, glow text-shadow |
| h1 | JetBrains Mono | 700 | 72 | 36 | line-height 1.05, tracking -0.02em |
| h2 | JetBrains Mono | 600 | 46 | 23 | tracking -0.015em |
| h3 | JetBrains Mono | 600 | 22 | 11 | amber |
| card value | JetBrains Mono | 700 | 22 | 11 | mint |
| lede | Geist | 300 | 18 | 9 | line-height 1.7, max 62ch |
| code box | JetBrains Mono | 400 | 14 | 7 | line-height 1.85 |
| card description | Geist | 400 | 13 | 6.5 | line-height 1.6 |
| window chrome | JetBrains Mono | 400 | 11 | 5.5 | uppercase, tracking 0.18em |
| tag | JetBrains Mono | 400 | 11 | 5.5 | uppercase, tracking 0.1em, outlined |
| card label / footer | JetBrains Mono | 400 | 10 | 5 | uppercase, tracking 0.2-0.22em |

Other px values that appear in `example.html` (inline overrides, captions) are also part of the shipped scale; `scripts/lint_deck.py` reads them from there.

## Colour tokens (exact)

| Token | Value | Role |
|---|---|---|
| `--hc-bg` | `#0a0c10` | background |
| `--hc-surface` | `#12141a` | cards |
| `--hc-ink` | `#e4e2d8` | primary text |
| `--hc-ink2` | `#96949d` | labels, footer |
| `--hc-green` | `#7ed3a4` | mint: prompt, h1, values, primary accent |
| `--hc-cyan` | `#64dfdf` | '$' prompt glyph, function names |
| `--hc-amber` | `#e9c58a` | h3, keywords, warnings |
| `--hc-rose` | `#d4a0b9` | variables |
| `--hc-red` | `#ff6b6b` | negative tags |

## Signature devices (every deck must show them)
- Window chrome row: three traffic-light dots + shell path ('~/session · zsh · 118x42')
- '$ command' prompt line above every title; blinking block cursor after the cover title
- Background stack: 56px grid with radial mask, 4px scanlines (screen blend), vignette
- HUD cards: 2px corner brackets top-left (mint) and bottom-right (dim), radius 2px
- Code box with syntax colours (comment grey, keyword amber, string mint, function cyan, var rose)
- Uppercase outlined tags (mint / amber / red)
- Footer rule with uppercase micro-labels and 'NN / 08'

## Layouts
Seed: cover with prompt + cursor, section divider '// Why Now', 3+2 spec-card grid, command + code trace, SVG bar chart, big stat + 2 cards, install CTA with code, '// thanks' close.
Research (layouts.html): figure with caption, robot video with on-frame tags, equation with colour-linked terms, three-rule results table.

## Motion
hcRise: translateY(18px) + fade, 0.6s cubic-bezier(.16,1,.3,1), staggered 0.06s; cursor blink steps(2) 1s. Reduced motion disables both.

## For research talks
Fits robotics-software / systems demos in dark rooms. Gaps: glow and scanlines hurt projector legibility, no figure or maths layout, smallest labels 10px.

## Flags (information only; sizes stay as shipped)
- Card labels and footer 10px, chrome and tags 11px, card text 13px, code 14px, lede 18px: all below 24px (12pt).
- Glow text-shadow, scanlines and vignette reduce legibility on projectors; tell the user if the room is large.

## Demo content to delete
The seed's demo content must not survive into a real deck. Lint looks for: `OpenDesign`, `BYOK`, `od model`, `nexu-io`, `discord.gg`.

## How to use
1. Start from `example.html` and `layouts.html`. Replace content only.
2. Keep the `:root` tokens, font families and weights, every px size, letter-spacing, the devices and the script exactly as shipped.
3. Never substitute fonts or add colours outside the token table.
4. A slide type the theme lacks is composed from its existing classes and tokens.
5. For other output formats, see `../../references/porting.md`.
