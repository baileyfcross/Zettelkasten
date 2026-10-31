2026-10-31 13:15

Status: #baby

Tags: [[Java Arrays and Elementary Algorithms]]

# Java Two-Dimensional Array

A Java two-dimensional array is an array whose elements are references to row arrays. An expression such as `matrix[row][column]` first selects a row and then selects an element within that row; the outer array and every row therefore have their own lengths.

Creating a rectangular array allocates equal-length rows, which can represent a matrix. Nested loops visit its cells, and [[Matrix Multiplication]] can compute each result cell by multiplying corresponding entries from one input row and one input column and summing those products.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
