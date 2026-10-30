2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Stream Teeing Collector

The Java teeing collector sends every stream element through two downstream collectors and merges their two final results. It enables one traversal to compute paired aggregates such as a count and sum or two differently filtered lists.

The merge function determines the result type and can place the two partial results into a [[Java Record Type|record]] or another container. Teeing is a terminal collection strategy, unlike a stream gatherer, which defines a composable intermediate operation.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
