2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]] · [[Java Nested Types and Package Organization]]

# Java Classpath and JAR Hell

The classpath is the ordered set of directories and archives from which the JVM locates classes in a nonmodular application. Because a class name does not encode which archive version supplied it, missing classes, duplicate definitions, and incompatible transitive versions can appear only when a particular execution path loads them.

This family of conflicts is commonly called JAR hell. Build tools manage declared dependencies, but a resolved build can still contain an unintended version. The [[Java Platform Module System]] adds explicit names, dependencies, readability, and package exports so more structural conflicts can be detected before runtime.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
