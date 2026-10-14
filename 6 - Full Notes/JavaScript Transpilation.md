2026-09-30 00:32

Status: #baby

Tags: [[Modern JavaScript Language Features]]

# JavaScript Transpilation

JavaScript transpilation converts source written with newer language features into older JavaScript syntax that a wider range of browsers can interpret. It is source-to-source conversion rather than compilation to a binary executable.

Babel can translate [[JavaScript Arrow Function|arrow functions]], default parameters, modules, and JSX. Transpiling in the browser is useful for a small demonstration but adds runtime cost, so a production workflow performs the conversion beforehand and serves the generated files.

Transpilation is needed for new syntax because an older parser cannot load a syntax feature through ordinary code. A [[JavaScript Polyfill]] instead supplies missing runtime behavior using syntax the target already understands. Keeping transpilation in the build process lets authors use clearer new syntax while deploying an older equivalent where required.

# References

[[learningreact1.pdf]]

[[youdontknowjs_upandgoing.pdf]]
