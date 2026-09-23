2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]]

# Unit of Work

A unit of work tracks changes made during one application operation and commits them together. An Entity Framework database context implements this pattern by tracking attached objects and generating the required statements when save is called. Separating it from the [[Repository Pattern]] lets repositories load or add [[Aggregate]]s while the application controls the commit. The unit of work should respect the aggregate's [[Transaction Boundary]] rather than combining unrelated domain operations merely because one database can do so.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
