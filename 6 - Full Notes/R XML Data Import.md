2026-10-04 22:20

Status: #baby

Tags: [[R Data Interchange and External Formats]]

# R XML Data Import

R XML data import parses an XML document into a tree whose elements, attributes, and text can be selected and converted into R values. A simple repeated-record document may map directly to a table, but a general XML hierarchy must be traversed according to its schema rather than flattened blindly.

The same structural distinction applies when exporting an [[R Data Frame]] to XML: row and column values need an explicit element layout so another program can reconstruct their meaning.

# References

[[rprimer.pdf]]
