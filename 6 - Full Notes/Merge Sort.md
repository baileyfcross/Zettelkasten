2026-09-06 00:13

Status: #baby

Tags: [[Sorting Algorithms]] [[Abstract Data Structures]]

# Merge Sort

Merge sort divides an unsorted collection into smaller groups until every group contains one trivially sorted item. It then repeatedly applies a [[Merge Operation]] to combine sorted groups into larger sorted groups.

This [[Divide and Conquer]] structure gives $O(n\log n)$ [[Time Complexity]]. Independent subgroups can be processed on different computers or processors before their results are merged, making the method suitable for large parallel sorts.

For a [[Linked List]], the merge operation can relink nodes in sorted order rather than repeatedly moving array elements. The algorithm remains stable when equal keys are taken from the left input first, preserving their earlier relative order.

For arrays, a reusable auxiliary buffer avoids allocating a fresh array at every recursive call, although the algorithm still requires $O(n)$ extra storage. Its predictable worst-case time and merge phase make it a foundation for [[External Sorting]], where ordered runs are produced separately and combined after data has moved through disk, a network, or distributed workers.

# References

[[algorithms.epub]]

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
