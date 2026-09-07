2026-09-06 20:34

Status: #baby

Tags: [[Web Data Query and Presentation]]

# Data Filtering

Data filtering restricts a result set to records matching a supplied condition. Applying the filter on the server before paging reduces the number of rows counted, transferred, and displayed.

A client search control can pass a filter value to an API, which composes it into an [[IQueryable]] before execution. Input and field choices must be constrained so filtering does not introduce a [[SQL Injection]] path.

# References

[[aspnetcore3andangular9_3ed.pdf]]
