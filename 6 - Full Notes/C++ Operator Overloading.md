2026-10-07 17:18

Status: #baby

Tags: [[C++ Scientific Programming]]

# C++ Operator Overloading

C++ operator overloading supplies a class-specific implementation for an existing operator. A matrix or vector class can thereby express addition, indexing, assignment, or multiplication with notation resembling the underlying mathematics.

The notation does not change operator precedence or create a new operator. Its implementation should preserve a predictable meaning for the class; overloaded indexing, for example, may validate bounds before returning the requested component.

# References

[[statisticalcomputingincplusplusandr.pdf]]
