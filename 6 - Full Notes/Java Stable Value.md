2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java Stable Value

The Java 25 preview described by the book calls a thread-safe, one-time, lazily initialized value a stable value. Its wrapper computes an expensive component on first demand, prevents reassignment, and lets the JVM treat later access more like a constant for optimization.

Stable values suit configurations, parsers, lookup tables, and expensive factory objects whose identity remains fixed. They are not appropriate for database connections, sockets, or other resources with an independent lifecycle, and visibility should force access through the initialization method.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
