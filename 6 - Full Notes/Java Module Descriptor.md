2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Module Descriptor

A Java module is described by `module-info.java` at the root of its source tree. The descriptor gives the module a unique name and contains directives that declare dependencies, exported packages, reflective access, and service-provider relationships.

The compiler turns this source descriptor into module metadata used during compilation and launch. Every named module implicitly reads `java.base`; other relationships must be stated. A minimal empty descriptor creates a named boundary, while a useful descriptor makes the module's required inputs and intended public surface explicit.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
