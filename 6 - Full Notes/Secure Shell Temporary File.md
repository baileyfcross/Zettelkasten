2026-10-12 00:45

Status: #baby

Tags: [[Shell Script Security and Reliability]]

# Secure Shell Temporary File

A secure shell temporary file is created atomically with an unpredictable name and restrictive permissions, commonly through a facility such as `mktemp`. This prevents another user from pre-creating a predictable path or redirecting the script through a symbolic link in a shared temporary directory.

The script should arrange cleanup on normal exit and relevant signals while avoiding deletion of an unverified path. Sensitive temporary content remains subject to storage, backup, and process-access risks even when the filename is safe.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
