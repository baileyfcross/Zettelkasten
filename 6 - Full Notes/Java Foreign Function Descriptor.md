2026-10-30 16:54

Status: #baby

Tags: [[Java Low-Level Platform and Native Performance]]

# Java Foreign Function Descriptor

A Java foreign-function descriptor states the native return and parameter layouts used to create a foreign method handle. It bridges Java's type system with the memory-level signature expected by a C function.

The descriptor is part of the contract between [[Java Native Symbol Lookup and Linker|symbol lookup and linking]] and the data stored in memory segments. Even a simple native call requires this explicit description; callbacks and array-processing functions add further conversions in both directions.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
