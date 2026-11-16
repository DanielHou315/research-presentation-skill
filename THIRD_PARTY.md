# Third-party material

The plugin's own code and text are MIT (see `LICENSE`). The five slide themes in
`skills/research-talk-crafter/themes/` are vendored, unmodified, from the
[Open Design](https://github.com/nexu-io/open-design) repository (commit `0701042f`, 2026-11-16)
and keep their own licences. Each theme folder holds its upstream `LICENSE` plus
`LICENSE-APACHE-2.0-OpenDesign`.

| Theme folder | Upstream | Licence | Copyright |
|---|---|---|---|
| `notebook-tabs` | [zarazhangrui/frontend-slides](https://github.com/zarazhangrui/frontend-slides) "Notebook Tabs", via Open Design `fs-notebook-tabs` | MIT | © 2025 Zara Zhang |
| `pentagram-grid` | [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) `ppt-pentagram`, extended by Open Design | MIT (+ Apache-2.0 for Open Design's changes) | © 2026 alchaincyf |
| `product-launch` | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) `product-launch`, restyled by Open Design | MIT + Apache-2.0 | © 2026 lewis; Open Design (Powerformer, Inc.) |
| `tech-sharing` | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) `tech-sharing`, restyled by Open Design | MIT + Apache-2.0 | © 2026 lewis; Open Design (Powerformer, Inc.) |
| `cyber-terminal` | [lewislulu/html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) `hermes-cyber-terminal`, via Open Design | MIT + Apache-2.0 | © 2026 lewis; Open Design (Powerformer, Inc.) |

Files in each theme folder:

- `example.html`, `UPSTREAM-SKILL.md`, `open-design.json`: upstream files, unmodified.
- `layouts.html`: a derivative work. It contains the upstream `<head>` and navigation script
  verbatim, plus new research slides and CSS written for this plugin.
- `THEME.md` and `../specs.json`: written for this plugin from the upstream source.

Fonts are loaded from Google Fonts at render time and are not bundled. All are SIL OFL 1.1
except Helvetica Neue (Pentagram Grid), a licensed system font that falls back to Arial.

`scripts/render_math.mjs` uses [KaTeX](https://github.com/KaTeX/KaTeX) (MIT) and
[MathJax](https://github.com/mathjax/MathJax-src) (Apache-2.0) if the user installs them; neither is
bundled.

Not used: Academic Paper and Kami (rejected by the maintainer); Beamer Metropolis/Moloch
(CC BY-SA 4.0) and Focus (GPL-3), whose ideas informed the research notes but whose code is not
included.
