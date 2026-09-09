2026-09-08 21:16

Status: #baby

Tags: [[.NET Files Streams and Serialization]]

# XML Serialization in .NET

XML serialization converts object state into an XML representation that can be stored or transported and later reconstructed. The shape of the output depends on the serializer, public members, type information, and any attributes used to control element and attribute names.

Serialization is a boundary contract rather than a substitute for a domain model. Applications should choose stable data-transfer shapes, understand which members are included, and treat incoming XML as untrusted input before allowing reconstructed data to influence behavior.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
