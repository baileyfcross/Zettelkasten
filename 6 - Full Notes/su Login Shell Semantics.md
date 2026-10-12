2026-10-07 18:14

Status: #baby

Tags: [[SLES Identity and Privilege Administration]]

# su Login Shell Semantics

The `su` command starts a shell under another user identity after the required authentication. Invoking it as a login shell also rebuilds the environment more like a fresh login, including the target user's home, path, and startup files; changing only the effective identity can retain more of the caller's environment.

This difference affects both behavior and diagnosis. A command that works after a full root login may fail under a partially retained environment, or inherited variables may expose unintended state. For one delegated administrative action, [[sudo Policy Delegation]] usually expresses scope more clearly than maintaining a broad root shell.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
