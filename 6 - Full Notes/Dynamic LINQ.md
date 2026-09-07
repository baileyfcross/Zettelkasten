2026-09-06 20:34

Status: #baby

Tags: [[Web Data Query and Presentation]]

# Dynamic LINQ

Dynamic LINQ constructs query operations such as ordering from runtime strings rather than fixed source expressions. This is useful when a client chooses a sort field that is not known until the request arrives.

The flexibility also creates risk. An API should validate a requested property against its permitted model fields and supply values separately instead of accepting an unchecked expression that could contribute to [[SQL Injection]].

# References

[[aspnetcore3andangular9_3ed.pdf]]
