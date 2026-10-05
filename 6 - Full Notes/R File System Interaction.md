2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R File System Interaction

R file system interaction lists directories, tests paths, creates or removes files and folders, and copies or renames filesystem objects. Relative paths are resolved from the [[R Working Directory]], so the same command can affect a different target when session context changes.

File operations should construct and inspect exact paths before mutating them. Interactive file choosers can locate an input during exploration, but recorded paths or project-relative conventions are needed for unattended reproducibility.

# References

[[rprimer.pdf]]
