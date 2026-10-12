2026-10-12 00:45

Status: #baby

Tags: [[Unix Text Stream Filters]]

# Head and Tail Stream Selection

`head` selects the beginning of a text stream and `tail` selects its end, usually by line count or byte count. Combining them can isolate an interior range without loading the entire file into an editor.

Tail can also follow a growing log, which changes it from a finite selector into a continuing stream source. Automation should account for that lifetime and for log rotation rather than assuming the process will terminate on its own.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
