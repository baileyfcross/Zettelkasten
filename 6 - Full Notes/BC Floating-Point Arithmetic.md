2026-10-12 00:45

Status: #baby

Tags: [[Shell Functions and Automation]]

# BC Floating-Point Arithmetic

The `bc` utility is an arbitrary-precision calculator language that supplies decimal arithmetic unavailable in ordinary Bash integer expressions. It can run interactively, execute a saved program, or receive an expression from a shell pipeline.

Scale and operation order determine the precision of fractional results. A script should pass only trusted or deliberately constructed expressions because sending unvalidated text into an interpreter turns data into executable calculator code.

# References

[[ultimatelinuxshellscriptingguide.pdf]]
