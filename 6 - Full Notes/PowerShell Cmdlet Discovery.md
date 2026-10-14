2026-10-12 00:45

Status: #baby

Tags: [[Alternative Shell and Cross-Platform Scripting]]

# PowerShell Cmdlet Discovery

PowerShell cmdlet discovery uses commands such as `Get-Command` to enumerate available commands and filter them by verb, noun, module, or command type. Consistent verb-noun names make related operations easier to locate than memorizing unrelated executable names.

Discovery reflects the modules installed and imported in the current session, so results can differ between hosts. A deployable script should declare and verify required modules rather than assume that command discovery on one workstation describes every target.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
