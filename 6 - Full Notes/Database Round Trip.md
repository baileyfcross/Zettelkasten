2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]], [[Web Performance and Scalability]]

# Database Round Trip

A database round trip is one request-response exchange between the application and its database. Each trip includes more than query execution: a connection path, command transfer, result transfer, and application-side processing all contribute latency.

Repeated queries inside a loop can make round trips grow with the number of parent records. Combining related work through joins or multiple result sets can reduce that cost when the resulting query and mapping remain manageable.

# References

[[aspnetcore3andreact.pdf]]
