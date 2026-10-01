2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Local Value

A Terraform local value assigns a name to an expression computed inside a module. It can normalize a [[Terraform Input Variable]], combine repeated naming components, or construct a map that several resources consume without exposing that intermediate calculation as part of the module's public interface.

Locals improve clarity when they name meaningful derived concepts, but they do not store mutable state and cannot be overridden by a caller. A local should not become a hidden configuration channel; values that consumers legitimately choose belong in inputs, while values that later automation needs belong in a [[Terraform Output Value]].

# References

[[masteringterraform.pdf]]

