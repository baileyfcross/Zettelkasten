2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Criteria API

The Jakarta Persistence Criteria API builds entity queries through typed Java objects rather than a query string. A CriteriaBuilder creates a typed CriteriaQuery, a Root identifies the queried entity, and predicates express conditions before the completed query is passed to an EntityManager for execution.

Criteria queries are more verbose than equivalent JPQL, but their programmatic structure fits search screens and other cases where conditions are assembled only when corresponding input values are present. Builder operations represent comparisons and logical clauses, allowing a query to accumulate a variable set of predicates while retaining type information about its result.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
