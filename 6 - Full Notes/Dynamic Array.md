2026-10-07 17:18

Status: #baby

Tags: [[Abstract Data Structures]]

# Dynamic Array

A dynamic array stores elements in contiguous memory while allowing its logical size to grow. When its current capacity is exhausted, it allocates a larger block, copies the existing elements, releases the old block, and redirects its storage pointer.

Growing by a multiplicative factor, such as doubling, spreads the occasional copying cost across many inexpensive insertions. Random indexed access remains constant time, but inserting in the middle requires shifting later elements and resizing invalidates pointers or iterators into the old block.

# References

[[statisticalcomputingincplusplusandr.pdf]]
