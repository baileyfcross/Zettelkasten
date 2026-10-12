2026-10-11 21:26

Status: #baby

Tags: [[Docker Development and Testing]]

# Container Unit Test Stage

A container unit test stage compiles and tests isolated code inside a build stage that contains the development toolchain. Failures stop the image pipeline before a runtime artifact is promoted, while successful output can be copied into a later stage.

The final image should not inherit test frameworks, source fixtures, compilers, or reports unless the running application needs them. This preserves test reproducibility without turning the production container into the test environment or expanding its attack surface.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
