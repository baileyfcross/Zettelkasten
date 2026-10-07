2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]] [[Abstract Data Structures]]

# Merge Sort

Merge sort divides an unsorted collection into smaller groups until every group contains one trivially sorted item. It then repeatedly applies a [[Merge Operation]] to combine sorted groups into larger sorted groups.

This [[Divide and Conquer]] structure gives $O(n\log n)$ [[Time Complexity]]. Independent subgroups can be processed on different computers or processors before their results are merged, making the method suitable for large parallel sorts.

For a [[Linked List]], the merge operation can relink nodes in sorted order rather than repeatedly moving array elements. The algorithm remains stable when equal keys are taken from the left input first, preserving their earlier relative order.

# References

[[algorithms.epub]]

[[statisticalcomputingincplusplusandr.pdf]]
