2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Binary Heap

A binary heap is a complete binary tree, commonly stored compactly in an array, whose parent key is ordered before the keys of its children. In a min-heap the smallest key is at the root.

Insertion places a new item at the next open leaf and moves it upward until the heap property is restored. Removing the minimum replaces the root with the last item and moves it downward, giving logarithmic insertion and extraction for a [[Priority Queue Pattern]].

# References

[[statisticalcomputingincplusplusandr.pdf]]
