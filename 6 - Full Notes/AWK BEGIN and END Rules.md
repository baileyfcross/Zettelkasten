2026-10-12 00:45

Status: #baby

Tags: [[AWK Text Processing]]

# AWK BEGIN and END Rules

An awk `BEGIN` rule runs before ordinary input records are processed, making it suitable for initialization, headers, and separator configuration. An `END` rule runs after input ends and can emit accumulated totals, summaries, or trailers.

These rules separate one-time setup and finalization from per-record logic. An early exit or input error may affect whether expected state exists, so summary code should not assume that valid records were processed.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
