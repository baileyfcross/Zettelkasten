2026-09-30 23:18

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Dependency Graph

Terraform builds a directed graph from references among resources, data sources, modules, and values. When one [[Terraform Resource]] uses another resource's output as an input, the producing object must be resolved first. Independent branches can proceed in parallel, while ordered edges constrain creation, update, and destruction.

This graph is what lets declarative configuration omit a hand-written procedure. An explicit `depends_on` is appropriate when an operational dependency exists but no value reference reveals it; excessive explicit edges obscure the real data flow and reduce safe parallelism. Values that cannot exist until execution remain unknown in the [[Terraform Plan]] and are resolved by [[Terraform Apply]].

# References

[[masteringterraform.pdf]]

