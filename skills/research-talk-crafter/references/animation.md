# Animation, video, 3D and interactive slides

Apply these only where your harness can produce them, using whatever mechanism it offers
(CSS, a slide tool's builds, PowerPoint animations, Beamer overlays, a JS runtime). The research
behind each rule, with sources, is in `animation-research.md`.

## When motion earns its place

| Helps | Hurts |
|---|---|
| Building a diagram one component per click | Decorative slide transitions (cube, swirl, zoom) |
| Pointing: highlight the part being discussed, dim the rest | Text flying in, bouncing bullets |
| A genuinely dynamic process: a trajectory, a rollout, an optimisation step | Ambient looping motion next to text people must read |
| Morphing one state into another while each part keeps its identity (before/after, an equation rewrite) | Morphs whose in-between frames are meaningless |
| Real video of robot behaviour | Anything on a timer the speaker can't control |

A well-annotated static diagram plus step-wise builds usually beats continuous animation when the
process is naturally a sequence of steps.

## Rules

**Control**
1. Every animation advances on the speaker's click. Nothing important happens on a timer.
2. The picture depends only on (slide, step). Jumping straight to a step, going backward, reloading
   and printing give the same frame. Use no wall-clock or unseeded randomness in visuals.
3. A click during an animation finishes it or retargets it; clicks never queue.
4. At most 5–7 steps per slide; beyond that, split the slide.

**Timing**
5. Fades and highlights take 200–350 ms; morphs and rearrangements 600–900 ms. Stage a complex
   morph in at most 2 stages (axes first, then data).
6. Use the theme's easing. All five themes use `cubic-bezier(.16,1,.3,1)` (ease-out).
7. Never make the speaker wait more than about 1 s for a stage to finish.

**Layout**
8. Reserve space for every step up front, so a later build never pushes earlier content around.
9. Animate position, scale and opacity, not layout dimensions.
10. Keep each mark bound to one thing through a morph, and give the same kind of change the same
    animation.

**Accessibility**
11. Never flash more than 3 times a second.
12. Respect reduced-motion settings where the harness exposes them: swap movement for an instant
    change or a short fade.
13. A looping video or animation in a deck that is read as a web page gets a pause control, or
    stops after a few loops.

**Video**
14. Muted, looping, with a poster frame; it starts when its slide is shown and stops when the
    slide is left.
15. Label speed, control mode and external aids on the frame itself (see SKILL.md section 4).
16. Keep a recorded fallback for any live demo.

**3D**
17. Create a scene only when its slide is shown, and dispose of it fully when the slide is left.
    Share one renderer across slides; browsers cap live WebGL contexts at about 16.
18. Render only while the slide is visible, and cap the device pixel ratio at about 1.5. Rehearse on
    the presenting laptop at projector resolution.
19. Every 3D slide has a still image used before it loads, when WebGL is unavailable, and in print.
20. Each step sets a declared camera pose or scene state; any orbiting the user does is reset on the
    next step.

**Interactive widgets**
21. The default state already makes the point, so the slide works if nobody touches it.
22. Widgets never take the clicker's keys (Page Up/Down, arrows) and reset when the slide is entered.
23. Interactive states can also be reached by steps (step 2 = slider at 0.3), and print shows a
    static value ("k = 0.3").

**Export**
24. Printed or exported versions show every slide at its final step, with stills in place of video,
    3D and widgets.
