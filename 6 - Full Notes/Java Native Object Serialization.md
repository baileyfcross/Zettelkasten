2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Native Object Serialization

Java native object serialization writes the state of a `Serializable` object graph through `ObjectOutputStream` and reconstructs it through `ObjectInputStream`. A `serialVersionUID` identifies the expected class version, and `transient` excludes a field from the default serialized form.

The binary representation is tied to Java class structure and can invoke object construction hooks during deserialization. It is therefore unsuitable for untrusted input and brittle as a long-lived cross-system contract. Explicit JSON, XML, or another schema-controlled format is easier to inspect and evolve.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
