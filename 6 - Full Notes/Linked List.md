2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]] [[Abstract Data Structures]]

# Linked List

A linked list is a data structure whose nodes store payload data and a [[Pointer]] to the next node. The first node is called the head, and the last node points to null to mark the end.

Items need not occupy consecutive memory locations because each pointer supplies the address of the next item. [[Linear Search]] can traverse the list by following these links, while self-organizing methods can change node order after successful searches.

Insertion can splice a new node by changing a small number of links without shifting later elements. That advantage is balanced by sequential access, pointer storage, and the need to update the head and neighboring links carefully when a node is removed.

# References

[[algorithms.epub]]

[[statisticalcomputingincplusplusandr.pdf]]
