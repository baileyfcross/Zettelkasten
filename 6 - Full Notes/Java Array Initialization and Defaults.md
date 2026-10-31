2026-10-31 13:15

Status: #baby

Tags: [[Java Arrays and Elementary Algorithms]]

# Java Array Initialization and Defaults

A Java array variable may be declared before an array is created, initialized with an array initializer, or assigned an array produced by `new`. Creation fixes the array's length; the read-only `length` member reports that size throughout the array's lifetime.

Every newly created array element receives the default value of its component type. Numeric elements begin at zero, Boolean elements at `false`, character elements at the zero character, and reference elements at `null`. An explicit initializer replaces those defaults with the listed values and determines the array length from their count.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
