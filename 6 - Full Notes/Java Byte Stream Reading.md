2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Byte Stream Reading

An `InputStream` reads raw bytes from a file, network, process, or memory source. A read may return one byte, fill part of a buffer, or signal end of stream, so code must use the returned count rather than assume the buffer was completely populated.

Byte streams are appropriate for images, serialized objects, and other binary data. Text requires an `InputStreamReader` with an explicit character set. Buffering improves efficiency, and the stream must be closed even when processing throws.

`InputStream.transferTo(OutputStream)` provides a direct whole-stream copy operation, and Java 18 added the corresponding method directly on `FileInputStream`. It removes the manual read/write loop for a transfer but does not change ownership: both streams still require deliberate lifetime and error handling.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
