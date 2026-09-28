2026-09-27 22:21

Status: #baby

Tags: [[Terraform Infrastructure as Code]]

# Terraform Input Variable

A Terraform input variable supplies a value from outside a configuration so the same infrastructure definition can serve different environments or instances. A variable declaration can document its purpose, constrain its type, and optionally provide a default; a variable without a default must receive a value.

Configuration refers to the value through `var.<name>`, while callers can provide values through a `.tfvars` file or command-line option. Variables should express legitimate variation such as region, capacity, or name, while separate environments retain distinct [[Terraform State]] rather than being distinguished only by a mutable variable file.

# References

[[clouddevopsengineersguide.pdf]]

