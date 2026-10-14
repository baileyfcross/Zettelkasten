2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Shell Standard Error

Standard error is file descriptor 2, the conventional stream for diagnostics and error messages. It normally shares the terminal with standard output but remains a separate channel that can be redirected, captured, or discarded independently.

The separation lets a pipeline process valid output while failures remain visible to the operator. Merging the streams is sometimes useful for unified logs, but it should be deliberate because diagnostic text can corrupt a downstream data format.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
