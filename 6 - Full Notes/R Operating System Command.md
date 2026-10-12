2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Operating System Command

An R operating system command launches an external program or shell command and can capture its status and text output. This extends an R workflow beyond the language, but command names, quoting, path syntax, and available executables differ across operating systems.

Arguments should be passed without constructing unsafe shell text from untrusted data. A portable analysis should isolate platform-specific behavior and check the returned exit status rather than assuming that command invocation implies success.

# References

[[rprimer.pdf]]
