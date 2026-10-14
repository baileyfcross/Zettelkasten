2026-10-11 21:26

Status: #baby

Tags: [[Docker Image Engineering]]

# Dockerfile Cache Ordering

Dockerfile cache ordering places stable and expensive build inputs before frequently changing application content. For example, copying dependency manifests and restoring packages before copying source code lets the dependency layer remain reusable when only implementation files change.

Every instruction depends on the state produced before it, so an early change invalidates that instruction and the later chain. A narrow [[Build Context]], an effective `.dockerignore`, deterministic dependency inputs, and deliberate instruction order reduce transfer, rebuild time, and accidental inclusion without changing the final runtime behavior.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
