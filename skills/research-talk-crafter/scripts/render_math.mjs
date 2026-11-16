#!/usr/bin/env node
// Render a LaTeX formula to MathML (via KaTeX) or to a self-contained SVG (via MathJax),
// for slide targets that can't run a math renderer themselves.
//
// Usage:
//   node scripts/render_math.mjs --mathml '\mathcal{L} = \lVert \epsilon - \epsilon_\theta \rVert^2'
//   node scripts/render_math.mjs --svg    '\mathcal{L} = ...' > eq.svg
//
// Needs `katex` (for --mathml) or `mathjax-full` (for --svg), resolved from the current
// directory, so install them where you run it:
//   npm install --no-save katex mathjax-full
//
// MathML output is native in current Chrome, Safari and Firefox and takes the theme's
// font-family and colour from CSS. SVG output draws glyphs as paths (no fonts needed).
// Colour-link terms with \textcolor{#hex}{...} using the theme's accent token.
import { createRequire } from "node:module";
import path from "node:path";

const require = createRequire(path.join(process.cwd(), "noop.js"));
const [mode, tex] = process.argv.slice(2);
if (!tex || !["--mathml", "--svg"].includes(mode)) {
  console.error("usage: render_math.mjs --mathml|--svg '<latex>'");
  process.exit(2);
}

if (mode === "--mathml") {
  const katex = require("katex");
  const out = katex.renderToString(tex, { output: "mathml", displayMode: true, throwOnError: true });
  // KaTeX wraps MathML in <span class="katex">; keep only the <math> element.
  const m = out.match(/<math[\s\S]*<\/math>/);
  console.log(m ? m[0] : out);
} else {
  const { mathjax } = require("mathjax-full/js/mathjax.js");
  const { TeX } = require("mathjax-full/js/input/tex.js");
  const { SVG } = require("mathjax-full/js/output/svg.js");
  const { liteAdaptor } = require("mathjax-full/js/adaptors/liteAdaptor.js");
  const { RegisterHTMLHandler } = require("mathjax-full/js/handlers/html.js");
  const { AllPackages } = require("mathjax-full/js/input/tex/AllPackages.js");
  const adaptor = liteAdaptor();
  RegisterHTMLHandler(adaptor);
  const doc = mathjax.document("", {
    InputJax: new TeX({ packages: AllPackages }),
    OutputJax: new SVG({ fontCache: "none" }),
  });
  const node = doc.convert(tex, { display: true });
  console.log(adaptor.innerHTML(node));
}
