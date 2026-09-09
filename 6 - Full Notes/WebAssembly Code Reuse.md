2026-09-08 22:09

Status: #baby

Tags: [[WebAssembly and Blazor Applications]]

# WebAssembly Code Reuse

WebAssembly code reuse means an existing library or application written in a compilable language may be adapted to run in the browser rather than rewritten from the beginning in JavaScript. The appendix uses a C game as an example of a potentially portable existing codebase.

Reuse is not automatic because user interface, host integration, and unsupported dependencies may still need new adapters. The compiled core is most reusable when it is already separated from operating-system-specific behavior.

# References

[[c8andnetcore30projectsusingazure.pdf]]
