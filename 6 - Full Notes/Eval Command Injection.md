2026-10-12 00:45

Status: #baby

Tags: [[Shell Script Security and Reliability]]

# Eval Command Injection

Eval command injection occurs when a shell passes attacker-controlled text to `eval`, causing that text to be parsed again as shell syntax. Characters that were initially data can become commands, redirections, substitutions, or control operators during the second interpretation.

The preferred defense is to avoid eval and represent commands as fixed code with values passed through quoted arguments or arrays. If dynamic evaluation is genuinely required, every component must originate from a constrained trusted source rather than from an attempted blacklist of dangerous characters.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
