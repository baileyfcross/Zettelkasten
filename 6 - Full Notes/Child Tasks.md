2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# Child Tasks

A task created while another task is running is not automatically part of its parent's completion. An attached child, created with the appropriate option, extends the parent's lifetime so the parent does not complete until the child has finished.

Attachment also affects how cancellation and exceptions are observed. Because implicit task hierarchies can surprise callers, structured asynchronous code should make ownership and waiting responsibilities explicit.

The default for many modern task-creation paths is detached behavior: a child can outlive the task that happened to create it. `AttachedToParent` deliberately extends the parent's completion and aggregates child failures into the parent relationship.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
