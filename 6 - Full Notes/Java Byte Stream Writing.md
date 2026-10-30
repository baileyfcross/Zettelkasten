2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Byte Stream Writing

An `OutputStream` writes raw bytes to a destination. File output streams and Files factories can create, replace, or append, while a buffered wrapper reduces the number of underlying writes for many small pieces.

Binary formats must define byte order, lengths, and structure independently of the stream itself. Writing a byte array does not make it self-describing, and character data should be encoded through a Writer or an explicit charset conversion. Closing or flushing completes buffered delivery but cannot guarantee every storage device has durably persisted the data.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
