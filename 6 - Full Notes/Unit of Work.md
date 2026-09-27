2026-09-22 20:53

Status: #baby

Tags: [[Aggregate Consistency and Persistence]] [[ASP.NET Core Service Layers and Mapping]]

# Unit of Work

A unit of work tracks changes made during one application operation and commits them together. An Entity Framework database context implements this pattern by tracking attached objects and generating the required statements when save is called. Separating it from the [[Repository Pattern]] lets repositories load or add [[Aggregate]]s while the application controls the commit. The unit of work should respect the aggregate's [[Transaction Boundary]] rather than combining unrelated domain operations merely because one database can do so.

For a RESTful service, the unit of work belongs at the application-operation boundary: the service coordinates repository changes and saves once, while the HTTP controller remains concerned with translating requests and responses.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
