2026-10-12 00:45

Status: #baby

Tags: [[AWK Text Processing]]

# AWK Record and Field

Awk reads input as records and divides each record into fields. The complete current record is `$0`, numbered field references such as `$1` select individual values, and `NF` reports how many fields were parsed.

The default record is a line and the default field separation treats runs of whitespace specially. Changing the separators makes the same pattern-action model operate on colon-delimited accounts, comma-like records, or multiline blocks.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
