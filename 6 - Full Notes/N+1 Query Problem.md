2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]]

# N+1 Query Problem

The N+1 query problem occurs when code retrieves a collection with one query and then issues another query for each returned item. Database round trips therefore grow with result size even when the final data could be retrieved more deliberately.

Dapper multi-mapping or multiple result sets can gather parent and child data in fewer trips. The replacement should still be measured because a single oversized query can introduce different costs.

# References

[[aspnetcore3andreact.pdf]]
