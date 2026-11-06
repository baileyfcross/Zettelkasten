2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java List Collection

A Java `List<E>` is an ordered collection that permits duplicate elements and supports position-based access. Its encounter order makes it suitable when insertion sequence or indexing is part of the data's meaning.

`ArrayList` stores elements in a resizable array and is efficient for indexed access and appending, while `LinkedList` represents a linked sequence and also implements deque operations. Programming to the List interface keeps those storage choices separate from code that only needs ordered collection behavior.

The implementation choice should reflect access patterns rather than the abstract possibility of insertion. `ArrayList` combines constant-time index access with cache-friendly iteration and amortized constant-time append, while a `LinkedList` insertion is only cheap after the node position is already known; repeated index-based access still performs linear traversal.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
