2026-10-30 16:54

Status: #baby

Tags: [[Java Low-Level Platform and Native Performance]]

# Java Native Upcall and Downcall

A foreign-function downcall invokes native code from Java through a linked method handle. An upcall makes a Java method available as a callable native callback, allowing a C routine to reenter Java during its operation.

The book's `qsort` example uses both directions: Java transfers an array into native memory and downcalls the C sorting function, while the native sorter upcalls a Java comparison method. The result is then read from the foreign memory segment back into a Java collection.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
