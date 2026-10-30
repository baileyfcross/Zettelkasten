2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Sequenced Set

`SequencedSet<E>` combines set uniqueness with a defined encounter order. It inherits the front, back, and reverse traversal contract of [[Java Sequenced Collection]] while retaining the rule that equal elements occur only once.

Its `reversed()` method covariantly returns another sequenced set, so callers keep the more specific set type without a cast. Ordered implementations such as `LinkedHashSet` and navigable sorted sets fit into this common hierarchy, whereas an unordered hash set cannot promise first and last elements.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
