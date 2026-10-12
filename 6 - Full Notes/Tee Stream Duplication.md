2026-10-12 00:45

Status: #baby

Tags: [[Shell Pipelines and Redirection]]

# Tee Stream Duplication

The `tee` utility reads standard input and writes the same data to standard output and one or more files. This allows a pipeline to retain an intermediate result or display it while continuing to feed later stages.

Because `tee` is a program in the pipeline rather than shell syntax, its own permissions and exit status matter. Appending versus replacing its output files should be chosen explicitly, especially when the retained stream is an audit record.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
