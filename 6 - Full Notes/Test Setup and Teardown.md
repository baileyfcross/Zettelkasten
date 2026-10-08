2026-09-27 11:46

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]] [[R Software Testing]]

# Test Setup and Teardown

Test setup creates the objects, data, and resources a case needs before its assertion runs. Teardown releases owned resources or reverses environmental changes after the case completes, including when the test fails.

Centralized setup reduces duplication only when the shared arrangement remains obvious to each test. Excessive implicit state makes a test harder to read and can couple cases that should be independent.

In R, teardown must run even when the test body raises an error. Registering restoration immediately after changing a global option or opening a connection prevents an early failure from skipping cleanup; scoped helpers can package the same pattern more readably. Files created by write-function tests belong in temporary locations and should not become hidden prerequisites for later tests.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[testingrcode.pdf]]
