2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]] [[REST Resource Contracts and Data Handling]]

# API Pagination

API pagination limits a collection response to a page selected by parameters such as page size and page index. The controller passes the requested window through the service and persistence layers rather than loading the entire collection for every client.

The response should make boundaries and navigation understandable, and the service should constrain unreasonable page sizes. Stable ordering is necessary so repeated pages do not arbitrarily omit or duplicate items as the query is evaluated.

The book's product-list example combines `page` and `per_page` with filters and a sort order, then returns both the selected products and a total count. The page is most useful when the response also lets a client understand the size and position of the result window.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]
