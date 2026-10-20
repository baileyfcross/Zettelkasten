2026-10-19 01:48

Status: #baby

Tags: [[Go Standard Library and Service Development]]

# Go Reader and Writer Interfaces

Go's `io.Reader` and `io.Writer` interfaces express byte-stream input and output through small method contracts. Files, buffers, compressors, network connections, and encoders can participate in the same pipelines when they satisfy those interfaces.

This structural composition lets an operation such as copying depend on capabilities instead of concrete resources. Wrapping a writer with compression or passing a file directly to a formatter changes behavior without changing the consuming algorithm's core contract.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
