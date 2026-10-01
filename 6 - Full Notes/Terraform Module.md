2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Module

A Terraform module is a directory of configuration evaluated as one scope. The directory where Terraform runs is the root module; referenced child modules encapsulate repeatable resource patterns behind [[Terraform Input Variable|inputs]] and [[Terraform Output Value|outputs]].

Effective modules are cohesive rather than merely large. They accept small configuration values, own resources that change together, and expose only the information consumers require. Repeating a well-designed module is often clearer than embedding several repetitions inside it. Modules from a registry or Git repository should use explicit versions, because an unreviewed interface change can alter resource addresses and force [[Terraform State Refactoring]].

# References

[[masteringterraform.pdf]]

