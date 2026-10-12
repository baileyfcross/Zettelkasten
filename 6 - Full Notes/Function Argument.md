2026-09-16 00:09

Status: #baby

Tags: [[R Function Design]] · [[R Scripts Functions and Debugging]]

# Function Argument

A function argument is the value supplied to a parameter when an R function is called. Arguments may be positional or named, and names improve clarity when a call has several options.

Validation near the function boundary can produce useful errors before invalid arguments contaminate later calculations.

The student companion treats the names in a function definition as placeholders whose values are supplied by each call. Its molar-mass example accepts parallel vectors of atom counts and atomic weights, making the data that control the calculation explicit rather than reading them from the workspace.

# References

[[essentialsofdatascience.pdf]]

[[rstudentcompanion.pdf]]
