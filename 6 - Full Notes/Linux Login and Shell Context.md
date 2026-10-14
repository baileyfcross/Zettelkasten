2026-10-07 18:14

Status: #baby

Tags: [[SLES Installation and Shell Operations]] [[Linux Shell Command Environment]]

# Linux Login and Shell Context

A Linux login establishes a user identity, home directory, working environment, groups, and command interpreter before interactive work begins. The prompt is therefore only the visible edge of a security and execution context: commands inherit the account's permissions, environment variables, current directory, and shell behavior.

Administrative diagnosis should confirm that context before interpreting a command result. A command run as root, through `sudo`, after `su`, or as an ordinary account may see different files and configuration. [[Linux Filesystem Navigation]] and shell history help make the active context explicit.

Bash additionally distinguishes login, interactive non-login, and non-interactive shell sessions. That distinction determines which global and per-user startup files are read, so an environment customization visible after login may not exist in a terminal tab or in a script launched by automation.

# References

[[ultimatelinuxshellscriptingguide.pdf]]

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
