2026-10-12 00:45

Status: #baby

Tags: [[Shell Functions and Automation]]

# Shell Function Positional Parameters

Shell function positional parameters are the arguments supplied at the function call, exposed inside the function through the same numbered and aggregate parameter syntax used by scripts. They temporarily replace the caller's positional view for the duration of the call.

This interface lets one function operate on different values without relying on global variables. Quoted aggregate expansion preserves each incoming argument when a function forwards them to another command.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
