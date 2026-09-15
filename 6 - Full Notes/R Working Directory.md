2026-09-14 20:21

Status: #baby

Tags: [[R Statistical Computing and Data Wrangling]]

# R Working Directory

The R working directory is the folder that file-reading and file-writing functions use when a relative path is supplied. `getwd` reports it and `setwd` changes it, although a project-centered workflow can establish the directory automatically.

Relative paths make an analysis easier to move when its code and data share a stable project structure. An unexplained working directory, by contrast, can cause the same script to read or create files in an unintended location.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
