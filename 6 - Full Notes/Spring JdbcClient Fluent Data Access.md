2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring JdbcClient Fluent Data Access

Spring `JdbcClient` builds a JDBC operation as a fluent sequence of SQL, named parameters, mapping, and cardinality. It wraps JdbcTemplate or NamedParameterJdbcTemplate but replaces overloaded query methods with terminal choices such as an optional result, one result, a list, or an update count.

Named parameters make bindings self-describing, and direct mapping to a Java record can remove a separate row-mapper class when columns correspond to components. The API remains blocking JDBC, so it belongs with Spring MVC or another imperative boundary rather than on a WebFlux event loop. SQL should stay encapsulated in a repository even when the fluent call is concise.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
