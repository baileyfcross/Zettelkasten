2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Collections Standard Library and File I-O]]

# Kotlin Collection Sorting

Kotlin collection functions can produce ascending or descending order from values with a natural ordering. Selector-based forms such as `sortedBy` derive the comparison key from each element, while comparator-based forms can encode a more specialized ordering.

The returned ordered result is distinct from the source collection unless a mutable in-place operation is deliberately used. Sorting therefore requires both an order policy and a decision about whether existing storage or a new result should carry that order.

# References

[[masteringkotlinforjavadevelopers.epub]]
