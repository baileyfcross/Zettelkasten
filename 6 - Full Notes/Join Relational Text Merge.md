2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Join Relational Text Merge

The `join` utility combines records from two text files when selected fields contain the same key. It resembles a simple relational join and can choose input key positions, output fields, and a field separator.

Both inputs normally need to be ordered consistently by the join field. Key normalization, duplicate keys, missing records, and locale-sensitive sorting all affect the result, so a reliable pipeline prepares and validates the inputs before joining them.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
