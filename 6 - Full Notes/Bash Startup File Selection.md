2026-10-12 00:45

Status: #baby

Tags: [[Linux Shell Command Environment]]

# Bash Startup File Selection

Bash selects startup files according to whether a shell is a login shell, an interactive non-login shell, or a non-interactive script. Global files can establish system-wide defaults, while files in a user's home directory apply personal environment and interactive customizations.

Distribution conventions differ, and one user file may source another to share configuration. A setting that appears in an interactive terminal is therefore not guaranteed inside a script; scripts should declare required inputs instead of depending on an unverified startup path.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
