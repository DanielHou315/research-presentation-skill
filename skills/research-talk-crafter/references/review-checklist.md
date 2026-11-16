# Review checklist (at most 3 fix rounds)

Run this before handing a deck over. Fix what fails, then re-check only what failed. After round 3,
stop and list the remaining issues for the user rather than looping. If you can start a fresh agent
or reviewer, have it run the checklist: a reviewer who didn't write the deck catches more.

## Checks

1. **Titles only.** List every slide title in order. Does the list alone tell the argument? Are
   content titles sentence claims, in one grammar? Any verdict or drama titles, or rhetorical
   questions?
2. **Glance test.** Can each slide's point be got in about 3 seconds? One point per slide?
3. **Density.** No paragraphs on slides (move them to notes); bullets within the theme's limit;
   evidence slides around 25 words, excluding axis labels.
4. **Figures.** Axes named and readable; direct labels; the proving element highlighted; the same
   colour for the same method across the deck; better-direction marked; error bars or trial counts
   shown; no pasted paper tables.
5. **Equations.** At most one per slide; every symbol defined; colour links match the diagram.
6. **Video.** Poster set; speed, control mode and aids labelled on the frame; at least one failure
   or uninterrupted take; success counts stated.
7. **Structure.** Motivation within the first 3 slides; closes on contributions; backup slides for
   the 3 most likely questions; slide count fits the time.
8. **Theme fidelity.** Only the theme's fonts, weights, px sizes and colour tokens; every signature
   device present; no leftover demo content from the seed. For HTML decks:
   `python3 scripts/lint_deck.py <deck.html> --theme <id>`.
9. **Accessibility.** Any colour you introduced passes `scripts/check_contrast.py` (4.5:1 for body
   text); nothing encoded by red/green alone; captions on narrated video.
10. **Animation** (if any). Jump to a random slide and step, go backward, reload: same picture each
    time? Nothing on a timer the speaker must wait for? No flashing over 3 times a second?
11. **Export.** A printed or PDF version shows every slide at its final step, with stills for video,
    3D and widgets, and nothing clipped at the slide edge.
12. **Rendered look.** If your harness can screenshot the deck, look at every slide once. Text
    running out of its box, overlaps and clipped words only show up rendered.

## Report

End with the titles list, what each round fixed, the remaining issues by slide number, any
bracketed placeholders left for the user, and any theme devices changed for the output format.
