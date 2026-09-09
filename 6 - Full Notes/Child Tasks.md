2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Child Tasks

A task created while another task is running is not automatically part of its parent's completion. An attached child, created with the appropriate option, extends the parent's lifetime so the parent does not complete until the child has finished.

Attachment also affects how cancellation and exceptions are observed. Because implicit task hierarchies can surprise callers, structured asynchronous code should make ownership and waiting responsibilities explicit.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
