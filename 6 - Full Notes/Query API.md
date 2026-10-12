2026-09-22 20:53

Status: #baby

Tags: [[CQRS Query and Read Model Design]]

# Query API

A query API exposes [[Application Query]] operations separately from state-changing command endpoints. Its routes and response contracts are organized around the information a client needs, such as browsing published items or viewing one item with owner details. The endpoint can return a [[Read Model]] directly and does not route the request through the [[Repository Pattern]] solely to reconstruct a behavioral aggregate. This keeps retrieval concerns independent of aggregate persistence.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
