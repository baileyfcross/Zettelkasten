2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# Closed Nested Transaction

A closed nested transaction may commit internally, but its effects remain part of the parent's tentative state and are not independently visible outside the nesting hierarchy. If the parent aborts, the inner effects are rolled back with it.

Closed nesting preserves strong isolation while allowing an inner failure to be retried without restarting unrelated inner work.

# References

[[bigdatamanagementandprocessing.pdf]]
