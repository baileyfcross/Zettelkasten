2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]]

# Shell Redirection and Pipelines

Shell redirection chooses where a command reads input and writes its standard output or standard error. A pipeline connects the standard output of one process to the standard input of another, allowing small commands such as filters and search tools to form a larger inspection or transformation.

The distinction matters when automation is expected to be reliable. Output intended as data should not be confused with diagnostic errors, and overwriting a file is different from appending to it. [[Bash Control Flow for Administration]] can use pipeline results and exit statuses to decide whether a later administrative step should run.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
