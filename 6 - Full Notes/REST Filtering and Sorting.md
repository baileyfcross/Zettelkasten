2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# REST Filtering and Sorting

REST filtering and sorting use query parameters to refine a collection without changing the identity of its resource type. A filter selects matching records, while a sort parameter states the attribute and direction used to order them.

The book combines category filtering, price ordering, and pagination in one product request. Supported fields and directions should be explicit and validated; accepting arbitrary expressions can make behavior unpredictable or pass unsafe input toward the data layer.

# References

[[masteringrestapis.epub]]
