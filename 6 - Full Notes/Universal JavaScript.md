2026-09-30 00:32

Status: #baby

Tags: [[Universal React Applications]]

# Universal JavaScript

Universal JavaScript is code that can execute without change in more than one runtime environment. A pure data transformation can run in a browser or Node.js, whereas direct use of `window`, the browser's request object, or a Node-only module ties code to one platform.

An application can isolate those platform adapters and keep the shared parsing, state transitions, and components universal. The source's distinction prevents an isomorphic file from being mistaken for entirely universal code: conditional branches may make the file work in both environments even though each branch itself is platform-specific.

# References

[[learningreact1.pdf]]
