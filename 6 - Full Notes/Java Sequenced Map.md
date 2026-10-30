2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Sequenced Map

`SequencedMap<K,V>` gives a map a defined encounter order for its entries. It supplies first and last entry access, end-specific insertion and removal, reverse traversal, and sequenced views of keys, values, and entries.

The abstraction lets ordered maps expose the same end-oriented vocabulary instead of forcing callers to know implementation-specific methods. As with [[Java Sequenced Set]], uniqueness remains part of the model—keys are unique even though their entries occupy a sequence.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
