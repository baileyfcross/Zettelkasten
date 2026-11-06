2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]] · [[Java Arrays and Elementary Algorithms]]

# Linear Search

Linear search examines items one at a time until it finds the target or exhausts the collection. It is also called sequential search.

For an unordered collection of $n$ items, the target could be last or absent, so the worst-case [[Time Complexity]] is $O(n)$. On a [[Linked List]], the algorithm begins at the head and follows each [[Pointer]] to the next node until it finds a match or reaches null.

In a Java array, the same algorithm advances an index from zero through `length - 1` and returns as soon as the indexed element equals the target. It does not require the array to be sorted.

Linear search can be the appropriate engineering choice for a small collection or an infrequent operation because it needs no preprocessing or auxiliary index. At larger scale or high request frequency, repeated scans can justify reorganizing data for key lookup, ordering it for [[Binary Search]], or building another search structure.

# References

[[algorithms.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
