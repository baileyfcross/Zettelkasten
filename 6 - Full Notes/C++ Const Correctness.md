2026-10-07 17:18

Status: #baby

Tags: [[C++ Scientific Programming]]

# C++ Const Correctness

C++ const correctness uses `const` declarations to state which values and object operations must not modify observable state. A const-qualified member function can be called on a constant object and promises not to change its non-mutable data members.

Const qualification documents intent and lets the compiler reject accidental mutation. In scientific code, read-only parameters should commonly be passed by const reference so large matrices or vectors are not copied while the called function remains unable to alter them.

# References

[[statisticalcomputingincplusplusandr.pdf]]
