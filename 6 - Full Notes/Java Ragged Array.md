2026-10-31 13:15

Status: #baby

Tags: [[Java Arrays and Elementary Algorithms]]

# Java Ragged Array

A Java ragged array is a multidimensional array whose row arrays have different lengths. Because a multidimensional array is implemented as an array of array references, each row can be allocated separately with the number of elements it actually needs.

Ragged storage can avoid unused cells when the represented structure is not rectangular. For example, a triangular portion of a symmetric matrix can use successively different row lengths, provided traversal consults each row's own `length` rather than assuming one global column count.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
