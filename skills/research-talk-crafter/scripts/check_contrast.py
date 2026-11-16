"""WCAG 2.x contrast checker for theme tokens.
Usage: python3 check_contrast.py BG FG [FG ...]   (hex colours)
Prints the ratio of each FG on BG and whether it passes 4.5:1 (body) / 3:1 (large)."""
import sys

def lum(h):
    h = h.lstrip('#')
    r, g, b = (int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)

def ratio(a, b):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)

if __name__ == '__main__':
    bg, *fgs = sys.argv[1:]
    for fg in fgs:
        r = ratio(bg, fg)
        print(f"{fg} on {bg}: {r:5.2f}:1  body {'PASS' if r >= 4.5 else 'FAIL'}  large {'PASS' if r >= 3 else 'FAIL'}")
