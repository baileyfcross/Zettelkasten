2026-10-30 16:54

Status: #baby

Tags: [[Java Low-Level Platform and Native Performance]]

# Java Vector API

The Java Vector API expresses platform-independent arithmetic over vectors of primitive values so the JVM can map supported operations to SIMD hardware. Vector values are loaded from arrays, combined with operations such as add or multiply, and written back to result arrays.

The API is an incubator module and is aimed primarily at libraries and performance-sensitive numerical code. It makes vector intent explicit, but ordinary scalar loops may already benefit from [[Java Auto-Vectorization]], so explicit vectors are justified only by measurement and unusual optimization needs.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
