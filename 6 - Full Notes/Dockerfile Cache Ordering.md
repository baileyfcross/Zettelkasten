2026-10-11 21:26

Status: #baby

Tags: [[Docker Image Engineering]]

# Dockerfile Cache Ordering

Dockerfile cache ordering places stable and expensive build inputs before frequently changing application content. For example, copying dependency manifests and restoring packages before copying source code lets the dependency layer remain reusable when only implementation files change.

Every instruction depends on the state produced before it, so an early change invalidates that instruction and the later chain. A narrow [[Build Context]], an effective `.dockerignore`, deterministic dependency inputs, and deliberate instruction order reduce transfer, rebuild time, and accidental inclusion without changing the final runtime behavior.

For a Maven application, the source copies `pom.xml` and resolves dependencies before copying the changing `src` tree. A source edit can then reuse the dependency layer, whereas copying all source before dependency resolution forces the expensive step back into the invalidated portion of the build.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[whendockermeetsjava_apracticalguidetodockerforjavaandspringbootapp.epub]]
