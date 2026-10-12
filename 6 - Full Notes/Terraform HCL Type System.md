2026-09-30 23:18

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform HCL Type System

Terraform configuration uses primitive values—strings, numbers, and booleans—and collection or structural values such as lists, sets, maps, tuples, and objects. Type constraints on a [[Terraform Input Variable]] document the expected shape and allow invalid configuration to fail before provider operations begin.

Simple values usually produce more durable module interfaces than deep objects that mirror an implementation. Structured content intended for another system can be assembled as native values and encoded with functions such as `jsonencode` or `yamlencode`, preserving validation and expression support until the boundary where text is actually required.

# References

[[masteringterraform.pdf]]

