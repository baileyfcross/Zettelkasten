2026-10-31 13:15

Status: #baby

Tags: [[Java Arrays and Elementary Algorithms]] · [[Java System Runtime Services]]

# Java System Array Copy

`System.arraycopy` copies a specified number of elements from a source array and offset to a destination array and offset. It performs the bulk transfer without an explicit Java loop and is useful when resizing an array into a newly allocated larger one.

Both arrays and both index ranges must be valid. A null source or destination, an out-of-bounds range, or an element that cannot be stored in the destination component type causes the corresponding runtime exception rather than a partial unchecked copy.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
