2026-10-11 21:26

Status: #baby

Tags: [[Docker Development and Testing]]

# Container Test Image Separation

Container test image separation keeps test code, frameworks, debuggers, and build tools in a test or builder artifact while the production image contains only the runtime application and required dependencies. Both can derive from the same source and build outputs without serving the same operational purpose.

This separation reduces production size and attack surface and prevents test-only entry points from becoming deployment interfaces. The pipeline should still record which tested output was copied into the runtime stage so the final artifact is traceable to the successful test run.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
