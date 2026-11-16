---
name: research-talk-crafter
description: Use when making, restyling or reviewing a research or academic presentation — conference talk, job talk, thesis or capstone defense, lab meeting, invited talk, lecture or tutorial, or a technical talk about research. Plans the talk, writes sentence-title slides with figure, equation and robot-video rules, and builds the deck in one of five locked themes, in whatever slide format the agent produces.
---

# Research Talk Crafter

This skill decides **what the talk says and how it looks**. It does not decide the output format
or which media can be used: your harness does. Build with whatever you normally produce (an HTML
deck, a .pptx file, Claude Slides, Codex slides, Keynote, Beamer, ...). Use video, animation,
embeds or 3D only if your harness supports them. When a style default of your harness conflicts
with this skill, this skill wins. When a technical limit of your harness conflicts, the limit wins:
route around it and tell the user what changed.

All paths below are relative to this skill's directory.

## 1. Before building

1. **Talk type, length, audience.** Infer them from the request; ask one short question only if a
   wrong guess is costly (a job talk or defense). Presets are in section 3.
2. **The one-sentence message.** Write the single sentence the audience should leave with. If the
   material doesn't yield one, propose one and ask.
3. **Speaker notes.** This is an operational choice, so ask the user whether they want notes and
   in what form. If they don't answer, write short bullet-point notes per slide.
4. **Slide plan.** For every slide, write down:
   - its role: hook, gap, method, evidence, limits or takeaway;
   - a sentence title that states the slide's claim;
   - the evidence medium (figure, video, diagram, equation, table);
   - a **"do not say"** line that names the overclaim to avoid.

   Share the list of titles before building. Read on their own, the titles must tell the whole
   argument. Cut any slide that leaves the audience where it found them.
5. **Theme.** Pick one of the five themes (section 5).

## 2. Content rules

These override generic "boardroom" deck defaults.

- **One message per talk, one point per slide.** If a slide's point needs two sentences, split
  the slide.
- **Sentence titles.** Every content slide's title is a full-sentence claim of at most 2 lines
  ("The contact-aware policy recovers from 3× more pushes than BC"), not a topic ("Results").
  Topic titles only on title, section, agenda and backup slides. No verdict or drama titles
  ("It's not X, it's Y", "The magic moment"), and no rhetorical questions as titles.
- **Evidence, not bullets.** The body is the figure, video, diagram, equation or table that proves
  the title, with at most two call-outs. If you must use bullets, keep to the theme's own limit
  (Notebook Tabs: 3 points) or at most 4, one line each.
- **Open fast.** Motivation, and what the audience will know by the end, come within the first
  1–3 slides. A short talk has no outline slide at the start; a roadmap after the motivation is
  fine, and talks over 20 minutes use section dividers.
- **Examples before generality.** Carry one running example through the talk.
- **Close on contributions,** not "Thank you" or "Questions?". Leave the contributions slide up
  during Q&A, and put backup slides behind it for the 3 most likely questions.
- **Honest results.** Show at least one failure case. State trial counts ("7/10 trials"). Compare
  against strong baselines.
- **No filler.** No invented numbers, quotes, names or citations: use `[bracketed placeholders]`
  and list them for the user. No stock imagery, icons used as content, or emoji. Delete all of the
  template's demo content (see each THEME.md).

Rationale, sources and disagreements between sources: `references/talk-craft.md`.

## 3. Talk-type presets

| Type | Length → slides | Shape |
|---|---|---|
| Conference talk | 12–20 min → 12–20 | hook + problem (2–3) · key idea (1–2) · method (3–5) · results (4–6, one point each) · contributions · backup |
| Job talk | 45 min → 35–45 | vision within 5 min · one deep contribution · 1–2 shorter ones · research agenda · contributions; keep ~80% accessible to non-experts |
| Thesis / capstone defense | 30–60 min | declarative thesis statement · the proposal's promises · evidence per chapter · answers to likely critiques in the main talk · limitations |
| Lab meeting / update | 10–20 min | last meeting's takeaways · status · raw results including failures · decisions or input needed; less polish |
| Invited / cross-field talk | 30–50 min | 30–40% background · teach one thing · ≥10 min Q&A |
| Lecture / tutorial | per session | objectives · key terms first · worked examples in steps · check-understanding · recap |
| Industry technical talk | 30–45 min | problem → what didn't work → what worked → metrics → decisions |

Pace: about 1 slide per minute for results-heavy talks; more slides when each is a light build.

## 4. Slide rules

- **Figures.** Redraw paper figures for the talk: fewer series, direct labels instead of legends,
  axes named and readable, and the element that proves the title highlighted while the rest is
  dimmed. **Use the same colour for the same method in every plot of the talk**; "ours" takes the
  theme's accent and baselines take neutrals. Mark which direction is better, and show error bars
  or trial counts.
- **Tables.** Never paste a paper table. At most 5 rows × 5 columns, three horizontal rules only,
  best result in the accent.
- **Equations.** At most one per slide and at most 3–4 terms visible. Define every symbol on the
  slide or aloud. Colour-link terms to the diagram using the theme's accent tokens. Derivations go
  to backup slides. Render with whatever your target supports (native MathML, KaTeX, Beamer, OMML);
  `scripts/render_math.mjs` converts LaTeX to MathML or SVG.
- **Robot / system video.** Label the frame itself with the playback speed ("4×"), the control mode
  (autonomous / teleop / scripted) and any external aids (mocap, fiducials). Include at least one
  uninterrupted take and at least one failure, and state the success count. Always set a poster
  frame. Use video only if your harness can embed or link it; otherwise use a still with a link.
- **Code.** At most 12 lines, in the theme's mono face, with the 1–3 lines that matter highlighted.

## 5. Themes (locked)

Five vendored templates. **Never invent a look and never fall back to your harness's default fonts.**

| Theme | Use for | Fonts |
|---|---|---|
| `themes/notebook-tabs` | thesis / capstone defenses, student talks, lectures | Bodoni Moda + DM Sans |
| `themes/pentagram-grid` | results-heavy talks, benchmark comparisons ("ours" = the red bar) | Helvetica Neue stack |
| `themes/product-launch` | job talks, invited talks, narrative openings | Fraunces + Outfit + JetBrains Mono |
| `themes/tech-sharing` | systems and robotics-software talks, code walkthroughs | Sora + IBM Plex Sans + IBM Plex Mono |
| `themes/cyber-terminal` | live tooling and demo talks in dark rooms | JetBrains Mono + Geist |

If the user names a theme or brings their own design system, use theirs.

How to use a theme:

1. Read `themes/<id>/THEME.md` (the exact spec: fonts and weights, px type scale, colour tokens,
   signature devices, layouts) and `themes/<id>/UPSTREAM-SKILL.md` (the template author's rules).
2. Start from `themes/<id>/example.html` (the seed deck) and `themes/<id>/layouts.html` (the
   research slides: figure, robot video, equation, results table).
3. **Replace content only.** Keep the colour tokens, font families and weights, **every px size as
   shipped**, letter-spacing, the signature devices and the navigation script exactly. Don't
   substitute fonts, add colours, round sizes or add chrome. A slide type the theme lacks is
   composed from its existing classes and tokens.
4. Every signature device listed in THEME.md appears in the deck.
5. **Other formats.** If you produce something other than HTML, follow `references/porting.md`.
   It says what must stay exact, how to rebuild devices your format can't express, and what to
   tell the user. `themes/specs.json` holds every value in machine-readable form.

Sizes stay as shipped. The templates are dense; if the user says the talk is for a large room,
point out the THEME.md flags and ask before changing anything.

## 6. Animation (only where your harness can animate)

Use whatever mechanism your harness offers. Full rules: `references/animation.md`.

- Animate only to **build** a diagram one part per click, to **point at** something (highlight and
  dim instead of a laser pointer), to show a **genuinely dynamic process**, or to **morph** between
  two states whose parts keep their identity. No decorative transitions.
- Builds advance on the speaker's click, and the picture depends only on (slide, step): jumping,
  going back, reloading and printing all show the same frame.
- Fades take 200–350 ms and morphs 600–900 ms, with the theme's easing: all five use
  `cubic-bezier(.16,1,.3,1)`. Use at most 5–7 steps per slide and reserve space for every step up
  front. Never flash more than 3 times a second.
- Video, 3D and interactive embeds always have a still fallback, and printed or exported versions
  show the final state.

## 7. Review before handing over (at most 3 rounds)

Run `references/review-checklist.md`. Where you can run Python on an HTML deck, also run:

```bash
python3 scripts/lint_deck.py <deck.html> --theme <id>   # fonts and sizes against specs.json, leftover demo text, placeholders
python3 scripts/check_contrast.py <bg-hex> <fg-hex> ...   # WCAG ratios for any colour you introduce
```

Fix what fails and re-check only that. After round 3, stop and report what remains. End the
hand-over with the titles list, any bracketed placeholders left to fill, and any theme devices you
had to change for the output format.
