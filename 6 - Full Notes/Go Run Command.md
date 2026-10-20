2026-10-19 01:48

Status: #baby

Tags: [[Go Program Structure and Toolchain]]

# Go Run Command

`go run` compiles and immediately executes Go source or a selected main package as one development operation. It provides a quick edit-build-run loop without leaving the program's final executable as the primary artifact.

The command still performs compilation and linking rather than interpreting Go source. It is therefore useful for experimentation, while [[Go Build Command|go build]] is the clearer boundary when a binary must be retained, inspected, or distributed.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
