2026-09-14 20:21

Status: #baby

Tags: [[R Statistical Computing and Data Wrangling]] · [[R Package Workspace and System Operations]] · [[R Scripts Functions and Debugging]]

# R Working Directory

The R working directory is the folder that file-reading and file-writing functions use when a relative path is supplied. `getwd` reports it and `setwd` changes it, although a project-centered workflow can establish the directory automatically.

Relative paths make an analysis easier to move when its code and data share a stable project structure. An unexplained working directory, by contrast, can cause the same script to read or create files in an unintended location.

The primer connects the working directory to listing files, selecting inputs, creating folders, and saving or loading workspace artifacts. Because all of those operations inherit the same path context, reporting the directory before a file mutation is a useful safeguard in an interactive session.

The student companion uses the working directory to locate scripts and data files and recommends keeping related work in a known folder. A source command that succeeds only after an unexplained directory change is not yet a portable script dependency.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[rprimer.pdf]]

[[rstudentcompanion.pdf]]
