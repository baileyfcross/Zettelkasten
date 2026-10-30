2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Sequenced Collection

`SequencedCollection<E>` is the Java collection interface for a defined encounter order with meaningful first and last elements. It extends `Collection` with uniform operations for adding, retrieving, and removing at both ends and for obtaining a reverse-order view.

The interface unifies capabilities that previously required collection-specific code. Lists and deques fit the sequence model directly, while mutating end operations can still reject changes when the concrete collection is immutable or does not support that placement.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
