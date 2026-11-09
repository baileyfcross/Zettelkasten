2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Data JPA Pagination

Spring Data JPA pagination passes a `Pageable`, commonly created with `PageRequest`, to a repository query and returns a page containing one bounded subset plus navigation metadata. Sorting can be included in the request so page boundaries have a deliberate order.

Pagination prevents an API from materializing an unbounded table in one response, but page-number stability depends on deterministic sorting and on how concurrent inserts or deletes affect the result set. Tests should verify both the selected content and page metadata rather than only checking that the repository returned some rows.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
