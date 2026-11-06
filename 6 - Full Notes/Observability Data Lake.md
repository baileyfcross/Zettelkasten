2026-11-06 12:32

Status: #baby

Tags: [[Observability Signals and Semantic Context]]

# Observability Data Lake

An observability data lake stores multiple operational signals so they can be searched, joined, aggregated, and analyzed as one evidence environment. Co-locating traces, metrics, logs, events, profiles, and real-user data makes it possible to overcome the blind spots of an individual signal and build analyses that span application, infrastructure, and business context.

The signals do not share one natural representation. Metrics have labeled counter, gauge, histogram, or summary structures; traces contain nested parent-child records; logs may be structured or free text; and profiles may be converted into metrics. An effective lake therefore preserves each signal's semantics while providing explicit transformations and query paths instead of flattening everything into undifferentiated text.

Different engines may still serve different workloads: relational time-series storage supports windows and joins, search indexes handle text and vector retrieval, and multidimensional stores support pre-aggregation. The architectural value is the governed correlation layer, not the claim that one database is ideal for every signal.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
