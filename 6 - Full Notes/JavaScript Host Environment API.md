2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Host Environment API

A JavaScript host environment API is functionality supplied by the runtime around the language rather than by the JavaScript specification itself. In a browser, globals such as `document` and functions such as `alert` expose browser facilities to JavaScript code.

The DOM method behind `document.getElementById`, the display work behind `alert`, and developer-console behavior may look like ordinary JavaScript objects and functions at the call site while being implemented by the browser. Separating language semantics from host APIs clarifies which behaviors travel between environments and which depend on a particular runtime.

# References

[[youdontknowjs_upandgoing.pdf]]
