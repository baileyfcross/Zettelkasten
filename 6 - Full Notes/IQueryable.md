2026-09-06 20:34

Status: #baby

Tags: [[Web Data Query and Presentation]]

# IQueryable

`IQueryable` represents a query whose operations can be composed before the data is retrieved. Filtering, sorting, counting, skipping, and taking can be assembled into one expression that the database provider translates and executes.

Deferred execution is important for [[Server-Side Paging]]: the application should narrow the query before materializing its results. Executing too early moves work and excess data into application memory.

# References

[[aspnetcore3andangular9_3ed.pdf]]
