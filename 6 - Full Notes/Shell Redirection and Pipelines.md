2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]] [[Shell Pipelines and Redirection]]

# Shell Redirection and Pipelines

Shell redirection chooses where a command reads input and writes its standard output or standard error. A pipeline connects the standard output of one process to the standard input of another, allowing small commands such as filters and search tools to form a larger inspection or transformation.

The distinction matters when automation is expected to be reliable. Output intended as data should not be confused with diagnostic errors, and overwriting a file is different from appending to it. [[Bash Control Flow for Administration]] can use pipeline results and exit statuses to decide whether a later administrative step should run.

At the descriptor level, standard input, standard output, and standard error are separate channels numbered 0, 1, and 2. Redirection changes their source or destination, while a pipeline connects one command's standard output to another command's standard input. Preserving the separation prevents diagnostic messages from being misread as data.

# References

[[ultimatelinuxshellscriptingguide.pdf]]

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
