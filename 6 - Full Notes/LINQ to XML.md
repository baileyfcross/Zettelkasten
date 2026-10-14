2026-09-08 21:16

Status: #baby

Tags: [[LINQ Query Construction]]

# LINQ to XML

LINQ to XML represents XML documents with objects such as `XDocument`, `XElement`, and `XAttribute`. Standard query operators can navigate, filter, project, and group nodes while construction syntax makes new XML trees composable from ordinary expressions.

Element names, namespaces, and missing content must be handled deliberately because XML structure carries meaning beyond text values. The model is convenient when a document fits in memory; forward-only XML readers remain preferable for very large streams.

The same object model supports query and mutation: code can locate elements with standard LINQ operators, construct new `XElement` trees, and add, replace, or remove nodes. This keeps XML transformations inside one composable in-memory representation.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
