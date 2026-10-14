2026-10-12 00:45

Status: #baby

Tags: [[Linux Shell Command Environment]]

# Shell Command History Expansion

Shell command history records prior interactive commands and supports recall, search, and history expansion. This reduces retyping, but replayed commands should be inspected because an old path, option, or privilege context may no longer be safe.

History is also a data-exposure surface. Secrets placed directly in command arguments may be written to a history file, so authentication material should be supplied through mechanisms designed to avoid command-line and history disclosure.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
