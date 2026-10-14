2026-10-12 00:45

Status: #baby

Tags: [[AWK Text Processing]]

# AWK Pattern-Action Rule

An awk pattern-action rule tests each input record against a pattern and executes the associated action when it matches. Either part may be omitted: an omitted pattern applies the action to every record, while an omitted action prints matching records by default.

Several rules can process the same record, allowing selection, transformation, and accumulation to remain separate. Regular-expression patterns, comparisons, and compound conditions should be chosen according to the record structure rather than compressed into one opaque expression.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
