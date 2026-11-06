2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Stack

A stack is an abstract data structure that removes items in last-in, first-out order. Its defining operations add an item to the top, inspect the top item, and remove the top item.

An array or a [[Linked List]] can implement the same interface. The abstraction is useful when only the most recently deferred task matters, as in reversing an order, matching nested structures, or recording a path for later backtracking.

An iterative [[Depth-First Search]] uses a stack to preserve unexplored branches, while recursive DFS uses the language call stack for the same last-in, first-out state. In Java, `ArrayDeque` is commonly preferred to the legacy `Stack` class for explicit stack behavior.

# References

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
