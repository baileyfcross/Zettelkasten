2026-11-06 13:25

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java HashMap Bucket Treeification

Java `HashMap` stores entries in an array of buckets selected from a spread key hash. Colliding entries initially form a linked chain within one bucket, so lookup can degrade toward linear time when many keys occupy the same location.

Modern Java implementations may convert a heavily populated bucket into a balanced red-black tree, improving operations within that bucket toward $O(\log n)$. Reaching the collision threshold alone is not sufficient: the backing table must also be large enough, because resizing a small table may distribute the entries more effectively than treeifying the bucket.

Treeification limits the damage from poor bucket concentration but does not remove the need for stable keys and correct `equals` and `hashCode` implementations. Average constant-time behavior still depends on effective hash distribution.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
