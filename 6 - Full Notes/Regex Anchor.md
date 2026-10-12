2026-10-12 00:45

Status: #baby

Tags: [[Regular Expressions and Stream Editing]]

# Regex Anchor

A regex anchor constrains a match to a position rather than consuming an ordinary character. The caret commonly anchors the beginning of a line and the dollar sign anchors its end, allowing a pattern to distinguish a whole-line structure from text that appears anywhere within a record.

Anchors are evaluated by the regex engine, so the shell should quote them to prevent unrelated interpretation. Combining both anchors can test an entire line, including the special case of an empty line.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
