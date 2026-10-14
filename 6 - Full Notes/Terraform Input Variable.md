2026-09-27 22:21

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Input Variable

A Terraform input variable supplies a value from outside a configuration so the same infrastructure definition can serve different environments or instances. A variable declaration can document its purpose, constrain its type, and optionally provide a default; a variable without a default must receive a value.

Configuration refers to the value through `var.<name>`, while callers can provide values through a `.tfvars` file or command-line option. Variables should express legitimate variation such as region, capacity, or name, while separate environments retain distinct [[Terraform State]] rather than being distinguished only by a mutable variable file.

A reusable [[Terraform Module]] benefits from small, atomic inputs instead of one large object that exposes its internal organization. Type constraints and validation can reject invalid configuration early, while defaults should represent genuinely optional decisions rather than conceal required deployment context.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
