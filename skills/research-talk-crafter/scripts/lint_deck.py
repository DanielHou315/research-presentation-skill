#!/usr/bin/env python3
"""Lint an HTML deck built from one of this skill's themes.

Usage:
    python3 scripts/lint_deck.py <deck.html> --theme <id> [--strict]

Checks (paths are relative to the skill directory; the script finds them itself):
  ERROR  font-size px values that are not in the theme's shipped scale
         (every px font size in themes/<id>/example.html, plus THEME.md's scale)
  ERROR  font families the theme doesn't use
  ERROR  leftover demo content from the template (themes/specs.json "demo_markers")
  WARN   hex colours that are not in the theme's seed
  WARN   [bracketed placeholders] still in the deck
  INFO   the slide titles in order (read them as a list: do they tell the argument?)

Exit code 1 if any ERROR (or any WARN with --strict). Standard library only.
"""
import argparse, html, json, pathlib, re, sys
from html.parser import HTMLParser

SKILL = pathlib.Path(__file__).resolve().parent.parent
GENERIC = {"serif", "sans-serif", "monospace", "system-ui", "ui-monospace", "cursive", "fantasy",
           "-apple-system", "blinkmacsystemfont", "inherit", "initial", "unset", "var"}


def font_sizes(text):
    sizes = set()
    for m in re.finditer(r"font-size\s*:\s*([0-9.]+)px", text):
        sizes.add(float(m.group(1)))
    for m in re.finditer(r"font-size=\"([0-9.]+)\"", text):
        sizes.add(float(m.group(1)))
    for m in re.finditer(r"clamp\(\s*([0-9.]+)px\s*,[^,]+,\s*([0-9.]+)px\s*\)", text):
        sizes.update({float(m.group(1)), float(m.group(2))})
    for m in re.finditer(r"--[a-z-]*size\s*:\s*([0-9.]+)px", text):
        sizes.add(float(m.group(1)))
    return sizes


def families(text):
    fams = set()
    for m in re.finditer(r"font-family\s*[:=]\s*\"?([^;\"}>]+)", text):
        for part in m.group(1).split(","):
            name = part.strip().strip("'\"").strip()
            if name and not name.startswith("var(") and name.lower() not in GENERIC:
                fams.add(name)
    for m in re.finditer(r"--font-[a-z]+\s*:\s*([^;]+);", text):
        for part in m.group(1).split(","):
            name = part.strip().strip("'\"")
            if name and not name.startswith("var(") and name.lower() not in GENERIC:
                fams.add(name)
    for m in re.finditer(r"--sans\s*:\s*([^;]+);", text):
        for part in m.group(1).split(","):
            name = part.strip().strip("'\"")
            if name and name.lower() not in GENERIC:
                fams.add(name)
    return fams


def hexes(text):
    return {m.group(0).lower() for m in re.finditer(r"(?<![&\w])#[0-9a-fA-F]{6}\b|(?<![&\w])#[0-9a-fA-F]{3}\b", text)}


class Titles(HTMLParser):
    """First heading-like element in each slide: h1/h2/h3, or a class naming a title, or a large inline size."""
    TITLE_CLASS = re.compile(r"\b(h1|h2|hc-h1|hc-h2|display|title)\b")

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.titles, self.in_slide, self.depth, self.capture, self.buf, self.found = [], False, 0, 0, [], False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        cls = a.get("class", "") or ""
        if tag == "section" and re.search(r"\bslide\b", cls):
            self.in_slide, self.found = True, False
        if not self.in_slide or self.found:
            if self.capture:
                self.capture += 1
            return
        if self.capture:
            self.capture += 1
            return
        style = a.get("style", "") or ""
        size = re.search(r"font-size:\s*([0-9.]+)px", style)
        if tag in ("h1", "h2") or self.TITLE_CLASS.search(cls) or (size and float(size.group(1)) >= 54 and tag == "div"):
            self.capture, self.buf = 1, []

    def handle_endtag(self, tag):
        if self.capture:
            self.capture -= 1
            if self.capture == 0:
                self.titles.append(re.sub(r"\s+", " ", "".join(self.buf)).strip())
                self.found = True
        if tag == "section":
            if self.in_slide and not self.found:
                self.titles.append("(no title found)")
            self.in_slide = False

    def handle_data(self, data):
        if self.capture:
            self.buf.append(data)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("deck")
    ap.add_argument("--theme", required=True)
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    args = ap.parse_args()

    specs = json.loads((SKILL / "themes" / "specs.json").read_text())
    theme = next((t for t in specs["themes"] if t["id"] == args.theme), None)
    if not theme:
        sys.exit(f"unknown theme '{args.theme}'; choose from: {', '.join(t['id'] for t in specs['themes'])}")
    seed = (SKILL / "themes" / args.theme / "example.html").read_text()
    deck_raw = pathlib.Path(args.deck).read_text()
    deck_text = html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<(style|script)[^>]*>.*?</\1>", " ", deck_raw, flags=re.S)))

    allowed_sizes = font_sizes(seed) | {float(r[3]) for r in theme["scale"]}
    allowed_fams = families(seed) | {f["family"].split(" (")[0] for f in theme["fonts"]}
    allowed_fams_l = {f.lower() for f in allowed_fams}
    allowed_hex = hexes(seed) | {c[1].lower() for c in theme["colors"] if c[1].startswith("#")}

    errors, warns = [], []
    bad_sizes = sorted(s for s in font_sizes(deck_raw) if s not in allowed_sizes)
    if bad_sizes:
        errors.append("font sizes not in the shipped scale: " + ", ".join(f"{s:g}px" for s in bad_sizes)
                      + f"\n         shipped: {', '.join(f'{s:g}' for s in sorted(allowed_sizes))}")
    bad_fams = sorted(f for f in families(deck_raw) if f.lower() not in allowed_fams_l)
    if bad_fams:
        errors.append("font families the theme doesn't use: " + ", ".join(bad_fams))
    demo = [m for m in theme.get("demo_markers", []) if m in deck_text]
    if demo:
        errors.append("leftover template demo content: " + ", ".join(demo))
    bad_hex = sorted(hexes(deck_raw) - allowed_hex)
    if bad_hex:
        warns.append("colours not in the theme's seed: " + ", ".join(bad_hex))
    placeholders = sorted(set(re.findall(r"\[[^\]\n]{1,60}\]", deck_text)))
    if placeholders:
        warns.append(f"{len(placeholders)} distinct [placeholders] left, e.g. " + ", ".join(placeholders[:8]))

    p = Titles()
    p.feed(deck_raw)
    print(f"Titles ({len(p.titles)} slides):")
    for i, t in enumerate(p.titles, 1):
        print(f"  {i:2d}. {t}")
    for e in errors:
        print("ERROR  " + e)
    for w in warns:
        print("WARN   " + w)
    failed = bool(errors) or (args.strict and bool(warns))
    print("FAILED" if failed else "OK")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
