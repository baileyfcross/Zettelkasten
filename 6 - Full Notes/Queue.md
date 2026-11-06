2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Queue

A queue is an abstract data structure that removes items in first-in, first-out order. New items enter at the back and the oldest available item leaves from the front.

Linked nodes or a circular array can implement the interface without shifting every remaining item after removal. Unlike a [[Stack]], a queue preserves arrival order, which makes it suitable for simulations of customers, jobs, packets, or events awaiting service.

The queue discipline defines the layer order of [[Breadth-First Search]]: newly discovered neighbors wait behind all vertices already found at the current or earlier level. Java can implement this traversal with `ArrayDeque`, avoiding the per-node overhead of `LinkedList` while retaining constant-time operations at both ends.

# References

[[statisticalcomputingincplusplusandr.pdf]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
