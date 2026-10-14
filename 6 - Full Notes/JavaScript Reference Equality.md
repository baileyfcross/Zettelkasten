2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Reference Equality

JavaScript compares two object, array, or function values by whether they refer to the same underlying object. Both `==` and `===` use reference identity for two non-primitive operands rather than recursively comparing their contents.

Two separately created arrays can therefore contain the same elements and still be unequal to each other. Coercion can produce a different result when an object is compared with a primitive, but that does not turn object-to-object equality into a structural comparison.

# References

[[youdontknowjs_upandgoing.pdf]]
