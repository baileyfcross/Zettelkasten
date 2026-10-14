2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Cut Field Extraction

The `cut` utility extracts selected character positions or delimited fields from each input line. Field mode combines an explicit delimiter with a field list, while character mode selects fixed positions independent of field boundaries.

Cut works well for simple records such as colon-delimited account files, but it is not a full CSV parser and does not understand quoting or embedded delimiters. Its usefulness depends on a stable, uncomplicated record format.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
