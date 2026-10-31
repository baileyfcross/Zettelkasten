2026-10-31 13:15

Status: #baby

Tags: [[Java Arrays and Elementary Algorithms]]

# Java Array Indexing and Bounds

Java array indexing is zero-based: the first element is at index `0`, and the final valid element is at `length - 1`. An index expression selects one element for reading or assignment, while a loop can traverse the valid range by advancing an integer index.

Access below zero or at least equal to the array length fails with an array-index-out-of-bounds exception. This boundary is why counted traversal normally tests `index < array.length` rather than allowing equality. The same rule applies independently to each row of a [[Java Two-Dimensional Array]].

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
