2026-10-31 13:15

Status: #baby

Tags: [[Java Arrays and Elementary Algorithms]] · [[Java Inheritance Composition and Object Contracts]]

# Java Array Cloning

Calling `clone()` on a Java array creates another array of the same runtime type and length. No cast is required for the returned array reference because array cloning uses a covariant return type.

The operation is shallow. Primitive element values are copied into the new array, but a reference-array clone contains copies of the original references, so corresponding positions in both arrays still designate the same objects. Deep duplication requires cloning or reconstructing the referenced objects as well.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
