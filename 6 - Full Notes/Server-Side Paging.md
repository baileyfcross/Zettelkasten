2026-09-06 20:34

Status: #baby

Tags: [[Web Data Query and Presentation]]

# Server-Side Paging

Server-side paging applies a page index and page size to a query before the result crosses the API boundary. The response returns only the requested records together with enough metadata, such as a total count, for the client to render navigation.

It reduces database materialization, network transfer, and browser rendering for large datasets. Page changes require new [[HTTP Request|requests]], so sorting and filtering parameters must be sent with the page selection.

# References

[[aspnetcore3andangular9_3ed.pdf]]
