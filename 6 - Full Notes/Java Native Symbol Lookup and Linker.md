2026-10-30 16:54

Status: #baby

Tags: [[Java Low-Level Platform and Native Performance]]

# Java Native Symbol Lookup and Linker

Foreign-function symbol lookup finds the address associated with a native library name such as C's `strlen` or `qsort`. A Java linker then combines that symbol with a declared native signature to create a method handle that Java can invoke.

The two steps separate locating code from describing its calling convention. Failure to find the symbol or a mismatch between the [[Java Foreign Function Descriptor]] and the native function is therefore exposed before or at the controlled call boundary rather than hidden behind a handwritten JNI wrapper.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
