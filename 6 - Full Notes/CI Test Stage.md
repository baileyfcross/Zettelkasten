2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# CI Test Stage

A CI test stage runs automated tests as part of the source-to-artifact build. Unit and other suitable tests provide evidence before the pipeline publishes a package for release.

The stage acts as a gate only for the checks it actually executes. A passing result means those defined expectations passed for that revision, not that every production behavior is known to be correct.

# References

[[aspnetcore3andreact.pdf]]
