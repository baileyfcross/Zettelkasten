2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Workspace Object Management

R workspace object management lists names in an environment, inspects selected objects, and removes objects that are no longer needed. Pattern and class-based filtering can narrow the inventory before deletion.

Removing all objects can produce a clean interactive state, but it is not a substitute for a script that constructs the required state from source data. Deletion should target verified names because object removal is immediate within the session.

# References

[[rprimer.pdf]]
