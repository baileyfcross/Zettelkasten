2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]] [[REST Resource Contracts and Data Handling]]

# API Pagination

API pagination limits a collection response to a page selected by parameters such as page size and page index. The controller passes the requested window through the service and persistence layers rather than loading the entire collection for every client.

The response should make boundaries and navigation understandable, and the service should constrain unreasonable page sizes. Stable ordering is necessary so repeated pages do not arbitrarily omit or duplicate items as the query is evaluated.

The book's product-list example combines `page` and `per_page` with filters and a sort order, then returns both the selected products and a total count. The page is most useful when the response also lets a client understand the size and position of the result window.

Pagination vocabularies may express the same window as offset and limit, page and records-per-page, or start and count. A portfolio should choose a consistent convention so consumers do not need to reinterpret equivalent collection navigation for every API they combine.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]

[[prorestfulapiswithmicronaut.epub]]
