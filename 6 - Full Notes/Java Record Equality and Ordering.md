2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Record Equality and Ordering

Java records automatically provide component-based equality and hash codes, but they do not automatically provide a natural ordering. A record placed in a `TreeSet` must implement `Comparable` consistently or the set must receive a suitable `Comparator`.

Ordering is consistent with equality when `compareTo` returns zero exactly for records that are equal. Comparing only a name while equality also considers age and city can cause distinct records to be discarded as duplicates. [[Java Comparable and Comparator Ordering]] can chain component comparisons to align both contracts.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
