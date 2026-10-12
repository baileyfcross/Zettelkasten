2026-09-27 11:46

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]] [[R Software Testing]]

# Test Case Isolation

Test case isolation ensures that one test's result does not depend on another test running first or leaving shared state behind. Each case arranges the state it needs and restores or discards that state when it finishes.

Isolation allows tests to run in any order and, where resources permit, in parallel. A failure that appears only after another test usually indicates hidden shared state rather than a trustworthy behavioral signal.

R tests need particular care around side effects such as global options, working directories, loaded packages, files, and graphics devices. A test should scope the temporary state and guarantee restoration even if an expectation fails; cleanup registered with `on.exit` or a scoped helper avoids contaminating later cases. External files and connections should likewise use temporary locations and deterministic teardown.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[testingrcode.pdf]]
