2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]]

# API Pagination

API pagination limits a collection response to a page selected by parameters such as page size and page index. The controller passes the requested window through the service and persistence layers rather than loading the entire collection for every client.

The response should make boundaries and navigation understandable, and the service should constrain unreasonable page sizes. Stable ordering is necessary so repeated pages do not arbitrarily omit or duplicate items as the query is evaluated.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
