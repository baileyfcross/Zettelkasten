2026-10-30 15:57

Status: #baby

Tags: [[Java Control Flow and Exceptions]]

# Java Enhanced-for Loop

The enhanced-for statement traverses each element of an array or `Iterable` without exposing an index or iterator variable. On each iteration, the loop variable receives the next element value.

It is appropriate when the body needs the elements but not their positions or iterator operations. Assigning a new value to the loop variable does not replace an array or collection element, because the variable receives a copy of the element value or reference. Index-sensitive updates require another traversal form.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
