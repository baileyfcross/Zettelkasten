2026-10-12 00:45

Status: #baby

Tags: [[Bash Variables and Control Flow]]

# Shell Positional Parameter

Shell positional parameters expose a script or function's invocation arguments by position. Parameter 0 identifies the invoked script or shell context, numbered parameters select individual arguments, and aggregate forms represent the complete argument set.

Quoted `"$@"` preserves each original argument as a separate word and is the usual choice when forwarding inputs. Unquoted aggregate expansion can lose boundaries around values containing spaces or wildcard characters.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
