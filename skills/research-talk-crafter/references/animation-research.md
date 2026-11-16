> Research notes behind `animation.md`, with sources. The rules to follow are in `animation.md`; section 6 here describes one hosting environment (Claude artifacts) and is background only.

# Animation in single-file HTML slide decks: research notes

Scope: 2D, 3D and interactive animation in self-contained HTML decks (Claude artifacts or plain web pages), sometimes exported to PDF/PPTX. Everything below is paraphrased; sources are linked inline.

---

## 1. What the research and presentation experts say

### 1.1 Animation is not automatically better than a good static picture

- **Tversky, Morrison & Betrancourt, "Animation: can it facilitate?" (IJHCS 2002)** — https://hci.stanford.edu/courses/cs448b/papers/Tversky_AnimationFacilitate_IJHCS02.pdf
  - Two principles: *congruence* (the graphic's structure should match the mental structure you want people to form; change over time naturally maps to animation) and *apprehension* (it must be perceivable and understandable; animations often fail because they are too fast or too busy).
  - Many studies that "showed" animation winning compared it with static graphics that carried less information (missing micro-steps), or confounded it with interactivity or prediction tasks. With information-equivalent statics, the advantage usually disappears.
  - People tend to think of continuous processes as a sequence of discrete steps, which static step diagrams match well; motion paths are often misperceived.
  - Recommendations: schematic over realistic; slow enough to follow; annotate (arrows, highlights); use discrete steps for discrete events; give viewers control (pause, replay). Animation is most defensible for real-time change and reorientation.
- **Mayer, Hegarty, Mayer & Campbell (2005), "When static media promote active learning"** — four experiments; annotated static illustrations with printed text matched or beat narrated animations (better on 4 of 8 comparisons, no difference on the rest). Their explanation: statics reduce extraneous load and invite more active processing. https://data.zhenzhi.com/details/1/864596096
- **Höffler & Leutner (2007) meta-analysis** (26 studies, 76 comparisons): moderate overall advantage for instructional animation (d ≈ 0.37), larger when the animation is *representational* (it depicts the thing being learned, not decoration), and largest for procedural-motor knowledge (d ≈ 1.06). Realistic video-like animation also did well. https://www.leibniz-ipn.de/en/research/publications/instructional-animation-versus-static-pictures-a-meta-analysis
  - Later update: Berney & Bétrancourt (2016, Computers & Education) found a smaller overall advantage (Hedges' g ≈ 0.23). https://doi.org/10.1016/j.compedu.2016.06.005
  - Takeaway: animation helps when the *motion itself is the content* (how a robot grasps, how a policy rolls out, how a gradient step moves a point). It does nothing, or harms, when it is decoration.
- **Robertson et al., "Effectiveness of animation in trend visualization" (InfoVis 2008)** — Gapminder-style animation was the least effective for *analysis* (small multiples were faster and more accurate) but was fast and enjoyable for *presentation*, albeit with many errors. https://www.microsoft.com/en-us/research/?p=145396
  - Takeaway for talks: animate to tell the story, then leave a static end-state (or small multiples) on screen long enough to read.

### 1.2 Mayer's multimedia principles relevant to slide animation

Summary page: https://edtechbooks.org/design_psychology/CTML ; Mayer 2020 overview PDF: https://ugc.futurelearn.com/uploads/files/7d/d6/7dd6188d-c343-4311-b064-ac98d2c95abc/Multimedia_Principles._R._E._Mayer__2020.pdf

- **Coherence**: remove extraneous material, including gratuitous animation. Decorative motion is a "seductive detail."
- **Signaling**: cue attention (highlight, zoom, dim others). This is the single best use of small animation in talks: a highlight that appears exactly when the speaker refers to something.
- **Segmenting**: break a continuous explanation into learner-paced chunks. In a talk, the presenter's click *is* the pacing control — so animations should be step-driven, not on a timer.
- **Temporal contiguity**: show the visual at the moment you say it. Builds/fragments implement this.
- **Spatial contiguity**: put labels on the diagram, not in a legend; animate labels with their objects.
- **Redundancy / modality**: don't make the audience read paragraphs while you speak; narration + graphics beats narration + graphics + same text.
- **Pre-training**: introduce the parts (components, names) before animating how they interact.
- **Seductive details**: meta-analysis of 58 studies (>7,500 students) — interesting-but-irrelevant material reliably hurt learning, especially when placed next to the relevant diagram. https://news.wsu.edu/2020/03/19/seductive-details-inhibit-learning/

### 1.3 Animated transitions between states (data/diagram morphs)

- **Heer & Robertson, "Animated Transitions in Statistical Data Graphics" (InfoVis 2007)** — https://homes.cs.washington.edu/~jheer/files/2007-AnimatedTrans-InfoVis.pdf
  - Animated transitions significantly improved object tracking vs. abrupt cuts; *staged* transitions (e.g. rescale axes first, then move values) generally beat doing everything at once.
  - Guidelines: intermediate frames must still be valid graphics; keep a mark bound to the same entity throughout (object constancy); same operation → same animation, different operations → visibly different; group things that change the same way; stagger to reduce occlusion; slow-in/slow-out easing; prefer simple translation/scale over rotation; about 1 s per stage.
- **Distill, "Communicating with Interactive Articles" (2020)** — animation is effective for state transitions, causality and narrative; interactivity can be distracting or unused; segmenting and details-on-demand help; costs are high. https://distill.pub/2020/communicating-with-interactive-articles/

### 1.4 Practitioner advice

- **Fatahalian, "Tips for Giving Clear Talks"** — one point per slide; tell the audience what to look for; lead them through figures step by step; surprises are bad; write transition sentences in notes because the click happens mid-sentence. (No anti-animation rule per se; builds serve "leading by hand".) https://www.csie.ntu.edu.tw/~johnson/files/cleartalktips.pdf
- **Winston, "How to Speak" (MIT)** — fewer words; avoid laser pointers and instead put arrows/highlights on the slide; props and visuals engage. Implication: a step that adds an arrow or highlight replaces the laser pointer. https://akos.ma/blog/how-to-speak-by-patrick-winston/
- **Grauman, preparing clear talks** (CVPR) — similar build-up advice. https://www.cc.gatech.edu/%7Eparikh/citizenofcvpr/static/slides/grauman_preparing_clear_talks.pdf
- **Morgan McGuire, presentation advice** — https://www.cs.williams.edu/~morgan/presentation-advice.pdf

**Synthesis: when animation helps vs hurts**

| Helps | Hurts |
|---|---|
| Build-up of a diagram one component per click (segmenting + temporal contiguity) | Slide-to-slide decorative transitions (cube, swirl, zoom) |
| Signaling: highlight/dim what you are talking about | Text flying in letter by letter; bouncing bullets |
| Showing a genuinely dynamic process (trajectory, rollout, optimization, data flow) | Ambient looping motion next to content the audience must read |
| Morphing one state into another so the audience tracks identity (before/after, equation rewrite, code change) | Morphs where intermediate frames are meaningless or misleading |
| Real video of robot behavior (procedural/motor knowledge) | Animation on a timer the speaker can't control |
| Staged, ~0.5–1 s, eased transitions | Many simultaneous moving parts; long (>1.5 s) waits |

---

## 2. Technical patterns in HTML slide frameworks

### 2.1 reveal.js
- **Fragments**: elements with class `fragment` step in before the next slide; effects such as fade-up, current-visible, semi-fade-out, highlight-*; explicit ordering with `data-fragment-index` (shared indices allowed); `fragmentshown` / `fragmenthidden` events; nested fragments chain effects. https://revealjs.com/fragments/
  - Model: visibility is a CSS class toggled by the step counter, so going backward just removes the class. That's why fragments are robust to backward navigation and jumping.
- **Auto-Animate**: put `data-auto-animate` on adjacent slides; reveal.js matches elements (by text/node type, `src` for media, or explicit `data-id`) and FLIP-animates position, size, color, padding etc. via transforms; unmatched elements fade in; `data-auto-animate-id` / `-restart` group sequences; duration default 1 s. https://revealjs.com/auto-animate
  - Model: state lives in two *separate DOM snapshots*; the engine interpolates. Each slide is a complete, printable end-state.
- **Media**: `data-autoplay`, auto-pause on leaving a slide, lazy `data-src` within `viewDistance`, iframes get `slide:start` / `slide:stop` postMessages. https://revealjs.com/media/
- **Keyboard**: per-key overrides, `null` to disable a key, `addKeyBinding`. https://revealjs.com/keyboard/
- **PDF**: `?print-pdf` + Chrome print; fragments print as separate pages by default (`pdfSeparateFragments: false` collapses them to the final state); `pdfMaxPagesPerSlide`; decktape as CLI alternative. https://revealjs.com/pdf-export

### 2.2 Slidev (Vue)
- `v-click` / `v-after` / `v-clicks`; positions relative (`'+1'`) or absolute (`3`); ranges like `[2,4]` (end exclusive) to show/hide in a window; `v-switch` for mutually exclusive states; `clicks:` frontmatter to override the count. https://sli.dev/guide/animations
- `v-motion` variants: `initial`, `enter`, `click-N`, `click-N-M`, `leave` — i.e., the element declares a target state *per click number*; the runtime resolves the active variant from `$clicks` and tweens to it. This is exactly the "state per step" model.
- Slide transitions can differ by direction (`forward | backward`) and include a View Transitions option.
- **Shiki Magic Move**: tokenizes code before/after, pairs tokens by diff, classifies move/enter/leave, FLIPs moved tokens, fades others. https://antfu.me/posts/shiki-magic-move
- **Export**: Playwright-based. Default one page per slide with clicks off; `--with-clicks` emits one page per click; `--wait` for slow content. https://sli.dev/guide/exporting

### 2.3 Code-first animation tools
- **Motion Canvas**: scenes are generator functions; `yield* beginSlide('name')` marks pause points; a Present mode steps between them. https://motioncanvas.io/docs/presentation . Because time is driven by the generator rather than wall-clock, a frame is reproducible (seek = replay to that point).
- **Manim Slides**: `self.next_slide()` inserts pause points; `next_slide(loop=True)` loops a segment until advanced (good for "idle" dynamics). Converts to reveal.js HTML; `--one-file` inlines videos as data URIs and `--offline` inlines JS/CSS; PDF export prints each slide's *last frame* by default; PPTX (experimental) embeds videos with first-frame poster. Notes: large videos load slowly over the web, possible glitches between slides. https://manim-slides.eertmans.be/latest/reference/sharing.html , https://www.manim.community/plugin/manim-slides
- **Remotion**: every frame is a pure function of the frame number; it renders frames in parallel, so `Math.random()` breaks output — use seeded `random(seed)`. Same discipline applies to slide animations that must survive jumping/printing. https://www.remotion.dev/docs/using-randomness
- **Theatre.js**: keyframed sequences with `sequence.position` (scrubbable) and `play()` / `pause()`; position can be driven externally (e.g., by step number). https://theatrejs.com/docs/0.5/manual/sequences
- **GSAP timelines**: `seek(timeOrLabel)`, `progress()`, `tweenTo(label)`, `tweenFromTo()`, `reverse()`, `pause()`. Pattern for slides: one paused timeline per slide with a label per step; on step change call `tweenTo('step3')` (animated) or `seek('step3')` (instant jump). Backward works for free. https://gsap.com/cheatsheet/

### 2.4 Browser-native APIs
- **CSS transitions**: simplest step model — set `data-step` on the slide and let CSS selectors define each element's state per step; transitions animate between them. Fully reversible, no JS state.
- **Web Animations API**: `element.animate()` returns an Animation with settable `currentTime`, `playbackRate`, `pause()`, `reverse()`, `finish()`, `cancel()`, `commitStyles()`, and a `finished` promise — so animations can be seeked and finished instantly when the presenter clicks fast. https://developer.mozilla.org/docs/Web/API/Animation
- **View Transitions API (same-document)**: `document.startViewTransition(update)` snapshots old/new DOM and cross-fades/morphs elements with matching `view-transition-name`. Names must be unique among rendered elements or the transition is skipped; starting a new transition skips the running one to its end (good for fast clicking); transition *types* allow forward/backward styling; feature-detect and fall back to a plain DOM update. https://developer.chrome.com/docs/web-platform/view-transitions/same-document
- **Performance**: animate `transform` and `opacity` (compositor-only); use `will-change` sparingly because each layer costs GPU memory. https://web.dev/articles/stick-to-compositor-only-properties-and-manage-layer-count

### 2.5 Making animation step-driven, deterministic, seekable

Common thread across reveal.js fragments, Slidev `v-motion`, GSAP labels, Remotion:

1. **State is a function of (slide, step)**, not of history. Going to slide 7 step 3 directly must produce the same picture as clicking there.
2. **Tweening is cosmetic**: on step change, animate from the *currently rendered* values to the target state; if another click arrives mid-tween, retarget (or finish instantly). Never queue animations.
3. **Backward = same function, lower step**. Optionally play the reverse transition, or just snap (many speakers prefer snapping backward).
4. **Jump (overview, slide number, hash, print) = snap** with no animation.
5. **No wall-clock randomness**: seed PRNGs; drive continuous loops from a time value that you can reset.
6. **Print/export = render the final step (or every step)** with animations disabled.

---

## 3. 3D in slides (three.js / WebGL)

- **Lazy init per slide**: create the scene when the slide (or its neighbor) becomes current; reveal.js uses `viewDistance` for the same idea with media. Do not build every 3D scene at load.
- **Context limits**: browsers cap active WebGL contexts (around 16 in desktop Chrome, fewer on mobile); exceeding it silently kills the oldest context. Prefer **one shared renderer/canvas** moved between slides, or scissor/viewport multiple views in one canvas. https://bugnet.io/blog/how-to-fix-too-many-active-webgl-contexts-oldest-context-will-be-lost
- **Dispose when off-slide**: three.js frees nothing automatically. Removing from the scene does not free GPU memory; dispose geometries, materials, textures (not freed by material.dispose), render targets, controls; check `renderer.info.memory` for leaks. To destroy a context fully: `renderer.dispose()`, `renderer.forceContextLoss()`, remove the canvas. https://threejs.org/manual/en/how-to-dispose-of-objects.html
- **Pause render loops**: run `requestAnimationFrame` only while the slide is active (and the tab visible; `document.visibilityState`). For mostly static scenes, render on demand: render once, then re-render on control `change` / resize via a `renderRequested` flag (also avoids the damping feedback loop). https://threejs.org/manual/en/rendering-on-demand.html
- **Pixel ratio**: cap `setPixelRatio(Math.min(devicePixelRatio, 1.5–2))`; Codrops suggests ~1 desktop / 1.5 mobile and lowering adaptively when FPS drops; `powerPreference: 'high-performance'`; drop antialias or postprocessing under load; bake lighting; instance repeated geometry. https://tympanus.net/codrops/2025/02/11/building-efficient-three-js-scenes-optimize-performance-while-maintaining-quality/
- **Projector laptops**: assume integrated GPU and 1080p mirrored output; projector mirroring can change DPR mid-talk, so listen for resize/DPR changes. Test on battery power.
- **Context loss**: call `preventDefault()` on `webglcontextlost` (otherwise it never restores), stop the loop, rebuild all GPU resources on `webglcontextrestored`; ignore stale async loads. https://wikis.khronos.org/webgl/HandlingContextLost
- **Static fallback**: every 3D slide needs a poster image (inline data URI or pre-rendered SVG/PNG) shown if WebGL is unavailable, in print/PDF, under reduced motion, or before init. Can be captured once with `canvas.toDataURL()` (needs `preserveDrawingBuffer` or capture right after render).
- **Determinism**: drive 3D animation by a per-step state (camera pose, joint angles) and a resettable clock, so jumping to a step reproduces the same view; let OrbitControls changes be temporary and reset on step change.
- **Offline/no CDN**: for offline talks, inline the library (three.js module minified is ~600–700 KB; fine under a 16 MiB artifact cap). For Claude artifacts, scripts may load from cdnjs/jsdelivr/unpkg, but inlining removes a network dependency in the venue.

---

## 4. Interactive elements during live talks

- **Focus stealing**: a focused `<input type=range>`, `<select>` or textarea consumes arrow keys/space, so the clicker or arrow key changes the slider instead of advancing (or the reverse: the deck's key handler eats keys the demo needed). Mitigations: deck key handler ignores events whose target is an editable/interactive element *except* for PageUp/PageDown (what clickers send); blur interactive controls on slide change and on Escape; make demo controls `tabindex="-1"` unless needed; use pointer events inside a demo region with `stopPropagation`.
- **Accidental input**: wheel/scroll or trackpad over a 3D canvas zooms the camera unexpectedly; disable wheel zoom by default or require a modifier; keep the slide from scrolling.
- **Presenter-triggered interactions**: the safest "interactive" slide is one whose interactions are also reachable by steps (step 2 = slider at 0.3, step 3 = slider at 0.9). The audience sees the effect even if you never touch the mouse; live dragging is a bonus.
- **Reset**: a visible small reset button and automatic reset on slide entry; state is (slide, step) + optional ephemeral user override that is discarded on navigation.
- **Demo failure**: keep a recorded backup (video or screenshots) for any live/remote demo; don't debug on stage; rehearse on the actual hardware. https://www.red-gate.com/simple-talk/career/how-to-avoid-demo-fails-when-presenting-at-tech-conferences/
- **Interactivity value**: prediction tasks and parameter sandboxes help understanding, but much interactivity goes unused and can distract; defaults must already show the interesting state. https://distill.pub/2020/communicating-with-interactive-articles/
- **Print/PDF**: interactive widgets must render a meaningful static snapshot: the default parameter values, with the control drawn as a labeled static value ("k = 0.3").

---

## 5. Accessibility and robustness

- **prefers-reduced-motion**: honor `@media (prefers-reduced-motion: reduce)` and `matchMedia(...).addEventListener('change', ...)`. Reduced does not mean none: replace movement with cross-fades or instant state changes; keep information-carrying change but swap the cue. Triggers to avoid: scaling/zooming, spinning, parallax/multi-speed motion, 2.5D plane shifts, peripheral motion near text. https://webkit.org/blog/7551/responsive-design-for-motion/ , https://web.dev/prefers-reduced-motion
- **WCAG 2.3.1 (A)**: nothing flashes more than three times in any one second (avoid saturated red flashes; keep flashing areas small). **2.2.2 (A)**: auto-starting motion lasting >5 s that runs alongside other content needs pause/stop/hide (looping robot videos: provide a pause or stop after a few loops in the web version). **2.3.3 (AAA)**: motion from interactions can be disabled. https://tetralogical.com/blog/2022/01/10/animations-and-flashing-content/ , https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide
- **Durations/easing**: UI feedback 100–400 ms; avoid >500 ms for UI (NN/g). Material: ~150–200 ms desktop, ~225 ms enter / ~195 ms exit, ease-out for entering, ease-in for leaving, standard ease-in-out for changes. https://nngroup.com/articles/animation-duration , https://m1.material.io/motion/duration-easing.html . *Explanatory* motion (a morph the audience must track) is longer: ~0.6–1 s per stage (Heer & Robertson). Practical deck defaults: fragment fade 250–350 ms; highlight 200 ms; morph/rearrange 600–900 ms; staged morph ≤ 2 stages.
- **Layout shift**: reserve space for every step's content from the start (hidden via opacity/visibility, not `display:none`), so later builds don't push earlier content around. Use absolute/grid placement for builds.
- **Print/PDF**: `@media print` → disable transitions/animations, render final step (or emit one page per step), replace canvases/videos with posters, show interactive controls as static values. Hosted artifacts block `window.print`, so the deck should also offer an "export view" (all slides stacked at final state) the user can print from a normal tab, or render via headless Chrome.
- **PPTX**: HTML animation does not survive; export as images per step (Slidev's approach), or embed MP4 for videos (Manim Slides' approach).
- **Video**: `<video muted playsinline loop autoplay preload="metadata" poster="...">`. Muted inline autoplay is permitted on iOS/Chrome; without `playsinline` iPhone goes fullscreen; offscreen autoplay video is paused. https://webkit.org/blog/6784/ . Play on slide enter, pause and rewind on exit (reveal.js does this automatically). In artifacts, media must be data:/blob: URIs, so keep clips short and small (H.264 MP4, a few MB, 720p).

---

## 6. Sandbox constraints for hosted artifacts (Claude artifacts)

From the artifact server's own guide (this session) and https://www.shareduo.com/blog/claude-artifact-not-loading-fix :

- One HTML document, up to 16 MiB. CSS/JS/data/images inline (data: URIs or inline SVG). Remote images do not load.
- Scripts allowed only inline or from cdnjs.cloudflare.com (preferred), cdn.jsdelivr.net/npm, unpkg.com, and a few others; stylesheets only inline or fonts.googleapis.com; fonts from fonts.gstatic.com or data: URIs. Blocked loads fail silently — so check that the library actually loaded and fall back.
- fetch/XHR/WebSocket to other hosts blocked.
- Sandboxed frame: no alert/confirm/prompt, no `window.print`, no downloads, no cross-site iframes; fullscreen and audio playback only from a click handler (catch refusal).
- localStorage/sessionStorage/IndexedDB may be missing or throw: wrap in try/catch, never required for correctness.
- Only a plain `#name` hash is passed through: use `#s12` style anchors for slide deep links, not `#/12/3` or query strings. (Encoding step in the hash, e.g. `#s12-3`, stays within the allowed character set.)
- Inline: the animation runtime you wrote, small libs (GSAP core ~70 KB min), posters, fonts you care about (or accept a system-font fallback). Load from allowed CDN only for big optional libs (three.js), with a static fallback if it fails.

---

## 7. Animation rules for a slide skill (do / don't)

**Purpose**
1. DO animate only when motion carries meaning: build-up of a diagram, signaling (highlight/dim), a genuinely dynamic process, or a morph that preserves identity between two states.
2. DON'T use decorative slide transitions (cube, zoom, swirl, flying text). Default transition between slides: none or a ≤200 ms fade.
3. DO prefer a well-annotated static diagram plus step-wise builds over continuous animation when the process is naturally discrete.
4. DO use real video for robot/physical behavior (procedural content is where animation helps most).
5. DON'T put ambient looping motion next to text the audience must read; no seductive details.

**Control and state**
6. DO make every animation step-driven by the presenter's click; nothing important happens on a timer.
7. DO make rendering a pure function of (slide, step): jumping directly to any step, going backward, or reloading must give the identical picture.
8. DO treat tweens as interpolation toward the target state; on a new click mid-tween, retarget or finish instantly. Never queue.
9. DO snap (no animation) on jumps, overview, hash navigation, and backward navigation (optionally a short reverse for single-step back).
10. DON'T use `Math.random()` or wall-clock time in visuals; seed PRNGs and drive loops from a resettable clock.
11. DO keep ≤ ~5–7 steps per slide; if more, split the slide.

**Timing and motion**
12. DO use: fades/highlights 200–350 ms; enters ease-out, exits ease-in; morphs/rearrangements 600–900 ms with ease-in-out; stage complex morphs (axes first, then data), ≤ 2 stages.
13. DON'T exceed ~1 s per stage or make the speaker wait for an animation to finish before speaking.
14. DO animate `transform` and `opacity` only (plus color); avoid animating width/height/top/left and layout.
15. DO reserve layout for all steps up front (opacity/visibility, absolute positioning) so builds never shift existing content.
16. DO keep a mark bound to one entity through a morph (stable `data-id`), keep intermediate frames valid, and use the same animation for the same kind of change.

**Accessibility**
17. DO honor `prefers-reduced-motion`: replace movement/zoom/rotation with instant changes or ≤150 ms cross-fades; pause autoplaying loops; show 3D posters.
18. DON'T flash anything more than 3 times per second; avoid large saturated red flashes and strobing comparisons.
19. DO give looping video/animation a pause control (or stop after a few loops) when the deck is consumed as a web page.

**3D**
20. DO lazy-init 3D per slide, share one WebGL renderer/canvas across slides, and fully dispose (geometry, material, textures, render targets, controls) when a scene is unmounted.
21. DO run the render loop only while the slide is active and the tab visible; prefer render-on-demand for static scenes.
22. DO cap `devicePixelRatio` at 1.5–2, avoid heavy shadows/postprocessing, and rehearse on an integrated-GPU laptop at projector resolution.
23. DO handle `webglcontextlost` (preventDefault, stop loop, rebuild on restore) and always ship a static poster fallback.
24. DO make each 3D step a declared camera pose/scene state; reset user orbiting on step change.

**Interactivity**
25. DO make interactive slides presenter-safe: deck keys must still work when a control is focused (handle PageUp/PageDown/arrow keys at the deck level, blur controls on slide change), and wheel/drag must not hijack navigation.
26. DO make interactive state reachable by steps too (step = preset parameter values), auto-reset on slide entry, and include a small reset button.
27. DO show the most informative state by default; the demo must make its point even if nobody touches it.
28. DO keep a static or recorded fallback for any live/remote demo.

**Export and hosting**
29. DO support print/export: disable all animation, render each slide at its final step (option: one page per step), swap canvas/video/widgets for posters or static values.
30. DO keep the deck self-contained: inline the runtime, posters, and small libs; load only from sandbox-allowed CDNs with a fallback; wrap storage in try/catch; use `#s12`-style hashes; keep embedded videos short, muted, `playsinline`, with a poster frame.

---

## 8. Reference architecture: step-driven animation in a single-file deck

Core idea: the deck owns `{slide, step}`. Each animated element declares its target state per step. Render is a pure function of `(slide, step)`; tweening is an optional visual interpolation from the currently rendered values to the target.

```html
<!-- Declarative: element states keyed by step ("2+" = step 2 onward, "1-3" = range) -->
<section class="slide" id="s7" data-steps="4">
  <svg viewBox="0 0 800 450">
    <g data-anim='{"0":{"opacity":0}, "1+":{"opacity":1}}'>…encoder…</g>
    <g data-anim='{"0-1":{"opacity":0}, "2+":{"opacity":1}}'>…decoder…</g>
    <circle data-id="tok" data-anim='{"0-2":{"x":120,"y":200}, "3+":{"x":620,"y":200}}' r="10"/>
    <rect class="hl" data-anim='{"0-3":{"opacity":0}, "4":{"opacity":1}}'/>
  </svg>
  <div data-scene="robot3d" data-poster="data:image/webp;base64,…"></div>
</section>
```

```js
// --- state machine -------------------------------------------------------
const deck = { slide: 0, step: 0, reduced: matchMedia('(prefers-reduced-motion: reduce)').matches };

function go(slide, step, {animate = true} = {}) {
  const prevSlide = deck.slide;
  deck.slide = clamp(slide); deck.step = clampStep(deck.slide, step);
  if (prevSlide !== deck.slide) { unmountScenes(prevSlide); mountScenes(deck.slide); blurControls(); animate = false; }
  render(deck.slide, deck.step, animate && !deck.reduced);
  setHash(`s${deck.slide + 1}-${deck.step}`);            // plain #name form
}
const next = () => deck.step < steps(deck.slide) ? go(deck.slide, deck.step + 1)
                                                 : go(deck.slide + 1, 0);
const prev = () => deck.step > 0 ? go(deck.slide, deck.step - 1, {animate: false})
                                 : go(deck.slide - 1, Infinity);  // previous slide, final step

// --- pure render ----------------------------------------------------------
function render(slide, step, animate) {
  for (const el of animatedEls(slide)) {
    const target = resolve(el.dataset.anim, step);       // pure: (spec, step) -> props
    tweenTo(el, target, animate ? durationFor(el) : 0);  // retargets any in-flight tween
  }
  for (const s of scenes(slide)) s.setStep(step, animate); // 3D/canvas get the same contract
}

function tweenTo(el, target, ms) {
  el._anim?.cancel();                                     // never queue: retarget
  if (!ms) return applyProps(el, target);
  el._anim = el.animate([currentProps(el), toKeyframe(target)],
                        {duration: ms, easing: 'cubic-bezier(.4,0,.2,1)', fill: 'forwards'});
  el._anim.finished.then(() => { applyProps(el, target); el._anim.cancel(); }).catch(() => {});
}

// --- 3D scene contract ------------------------------------------------------
// One shared renderer; scenes are factories that mount into it.
const scenesRegistry = {
  robot3d: () => ({
    mount(host, renderer) { /* build scene graph; read poster as placeholder until first frame */ },
    setStep(step, animate) { /* target camera pose / joint angles for this step; tween or snap */ },
    start() { /* rAF loop only while active && document.visible; or render-on-demand */ },
    stop()  { /* cancelAnimationFrame */ },
    unmount() { /* traverse + dispose geometry/material/textures/targets/controls */ },
  }),
};
function mountScenes(i) {
  if (!webglOK() || deck.reduced || printing) return showPosters(i);
  for (const host of sceneHosts(i)) { const s = scenesRegistry[host.dataset.scene]();
    s.mount(host, sharedRenderer()); s.setStep(deck.step, false); s.start(); host._scene = s; }
}
function unmountScenes(i) { for (const h of sceneHosts(i)) { h._scene?.stop(); h._scene?.unmount(); h._scene = null; } }
// sharedRenderer(): lazy-create once; setPixelRatio(min(dpr, 1.5)); handle webglcontextlost
// (preventDefault, stop) and webglcontextrestored (re-mount current slide).

// --- input safety -----------------------------------------------------------
addEventListener('keydown', e => {
  const k = e.key, inWidget = e.target.closest('input,select,textarea,[data-interactive]');
  if (['PageDown','ArrowRight',' '].includes(k) && !(inWidget && k !== 'PageDown')) { e.preventDefault(); next(); }
  if (['PageUp','ArrowLeft'].includes(k)     && !(inWidget && k !== 'PageUp'))   { e.preventDefault(); prev(); }
  if (k === 'Escape') document.activeElement?.blur();
});

// --- print / export -----------------------------------------------------------
// ?print (or a button) => for each slide: render(i, steps(i), false) (or one clone per step),
// stop all loops, swap scenes/videos/widgets for posters/static values, @media print { * { transition:none; animation:none } }.

// --- storage is optional --------------------------------------------------------
function safeStore(k, v) { try { localStorage.setItem(k, v); } catch {} }
```

Notes on the sketch:
- The state spec is data, so the same deck can be rendered at any step for thumbnails, overview grids, PDF pages, and backward navigation.
- Continuous dynamics (a looping rollout, a spinning model) are scene-internal and driven by a clock the scene resets on `setStep`; they do not affect the declared state, and they are paused under reduced motion and in print.
- For morphs between *different* DOM (equation/code rewrite), the same contract holds: step N picks which DOM variant is visible; a FLIP pass (or `startViewTransition` with stable `view-transition-name`s, feature-detected) animates matched elements; a new click skips the running transition to its end.
- GSAP is a drop-in alternative to `tweenTo`: one paused timeline per slide with labels `step0..stepN`; `tweenTo(label)` for forward, `seek(label)` for jumps/backward.
