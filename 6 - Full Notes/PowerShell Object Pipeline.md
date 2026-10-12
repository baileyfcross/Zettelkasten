2026-10-12 00:45

Status: #baby

Tags: [[Alternative Shell and Cross-Platform Scripting]]

# PowerShell Object Pipeline

The PowerShell object pipeline passes structured objects with properties and types between commands rather than reducing every intermediate result to display text. Downstream cmdlets can filter, select, sort, and format properties without reparsing column spacing.

Formatting should remain at the end of the pipeline because formatted output is a presentation representation rather than the original object. Native Unix commands still exchange text, creating a boundary where conversion and parsing may be required.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
