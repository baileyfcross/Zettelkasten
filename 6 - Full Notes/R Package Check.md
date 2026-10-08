2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Package Check

An R package check validates the package as a distributable whole. It examines metadata and declared dependencies, parses code and documentation, runs examples, verifies expected files, and executes the tests connected through [[R Package Test Structure]].

The check should be run regularly and in more than one execution environment because operating systems, R versions, locales, file systems, and compiled dependencies can expose different defects. [[Continuous Integration]] can run these checks after each accepted change, while [[Code Coverage]] can reveal which exported behaviors still lack direct tests. A clean local test run is therefore evidence, but not a substitute for package-level and cross-platform checking.

# References

[[testingrcode.pdf]]
