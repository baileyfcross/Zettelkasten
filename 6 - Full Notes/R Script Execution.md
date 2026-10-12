2026-10-04 22:56

Status: #baby

Tags: [[R Scripts Functions and Debugging]]

# R Script Execution

R script execution evaluates saved expressions in their written order, either by sending selected lines from an editor or by sourcing the complete file. Running the whole script tests whether later objects and graphs can be recreated without relying on unrecorded console work.

Execution occurs in an environment, so existing objects can conceal missing setup steps. A clean-session run and an explicit [[R Working Directory]] expose dependencies that an interactive session may have supplied accidentally.

# References

[[rstudentcompanion.pdf]]
