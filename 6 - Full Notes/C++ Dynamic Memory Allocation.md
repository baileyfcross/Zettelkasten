2026-10-07 17:18

Status: #baby

Tags: [[C++ Scientific Programming]]

# C++ Dynamic Memory Allocation

C++ dynamic memory allocation obtains storage while a program is running, allowing array and object sizes to depend on data that was unavailable at compile time. The `new` forms return a [[Pointer]] to the allocated object or block.

Every successfully allocated block must have a clear owner and a matching release operation. Arrays require the array form of deletion, and copied objects that own raw dynamic storage need coordinated copy, assignment, and destruction behavior to prevent leaks, double deletion, or dangling pointers.

# References

[[statisticalcomputingincplusplusandr.pdf]]
