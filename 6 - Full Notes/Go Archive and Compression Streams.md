2026-10-19 01:48

Status: #baby

Tags: [[Go Standard Library and Service Development]]

# Go Archive and Compression Streams

Go separates archive containers from compression streams. The archive packages read and write formats such as tar and zip, while compression packages wrap readers or writers for gzip, zlib, DEFLATE, LZW, and related encodings.

Because these components implement stream interfaces, an application can layer a compressor over a file and use [[Go File Copy with io.Copy|io.Copy]] to move the content. Writers must be closed or flushed so format trailers and buffered bytes reach the underlying destination.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
