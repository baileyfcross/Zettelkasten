2026-10-30 16:54

Status: #baby

Tags: [[Java Structured Concurrency and Scoped Context]]

# Java All-Successful Structured Join

An all-successful structured join requires every subtask in a scope to complete successfully. If one task fails, the scope fails and interrupts siblings that are still running, preventing a partial result from being mistaken for a complete one.

The book distinguishes policies that return the homogeneous successful subtasks from a policy whose `join` returns no aggregate and leaves callers to read separately retained subtask handles. Both express the same all-or-fail requirement but expose results differently.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
