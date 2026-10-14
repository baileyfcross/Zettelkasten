2026-10-12 00:45

Status: #baby

Tags: [[Linux Shell Command Environment]]

# Shell Conditional Command List

A shell conditional command list uses the exit status of one command to determine whether another command runs. With `&&`, the next command runs after success; with `||`, it runs after failure. A semicolon merely sequences commands without making execution conditional on the preceding result.

Mixed `&&` and `||` lists should be kept short or grouped explicitly because their left-to-right behavior can be misread as an ordinary programming-language Boolean expression. For longer recovery or decision logic, [[Bash Control Flow for Administration]] makes the intended branches clearer.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
