2026-10-30 15:57

Status: #baby

Tags: [[Java File IO Serialization and Persistence]]

# Java Buffered Character Reading

A Java `Reader` decodes characters from an underlying source, and `BufferedReader` reduces repeated low-level reads while adding line-oriented operations. `Files.newBufferedReader` opens one for a Path and a selected character set.

Character decoding is part of the data contract; relying on an environment default can produce different text on another machine. Reading line by line avoids loading an entire large file, while `Files.readString` or `readAllLines` is convenient only when the content comfortably fits in memory.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
