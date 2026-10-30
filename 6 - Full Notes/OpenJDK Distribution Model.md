2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# OpenJDK Distribution Model

OpenJDK is the open development project and reference code base from which multiple organizations build Java Development Kit distributions. A Java version is therefore not synonymous with one installer: Oracle, Eclipse Temurin, Amazon Corretto, Azul, IBM, and other vendors can package compatible builds with different support and licensing arrangements.

Choosing a distribution is an operational decision as well as a language decision. The application should target a supported Java specification level, while the organization separately evaluates update availability, production licensing, platform coverage, and vendor support for its selected JDK.

The Java 25 source distinguishes the six-month feature cadence from vendor support policy: a release may introduce the same platform features across compatible distributions while long-term maintenance, installer availability, and commercial terms differ. Toolchain selection should therefore name both a Java version and a concrete maintained distribution.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
