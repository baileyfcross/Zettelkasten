2026-09-16 00:09

Status: #baby

Tags: [[R Function Design]] · [[R Scripts Functions and Debugging]]

# Function Local Variable

A function local variable is created inside a function's execution environment and normally disappears when the call ends. Local state prevents intermediate objects from cluttering or accidentally modifying the analyst's workspace.

Returning the intended result makes the function's output explicit while keeping implementation details internal.

The book contrasts these temporary values with global objects visible in the workspace. A locally calculated hypotenuse or molar mass disappears after the call except for the returned value, preventing intermediate names from accumulating in the analyst's session.

# References

[[essentialsofdatascience.pdf]]

[[rstudentcompanion.pdf]]
