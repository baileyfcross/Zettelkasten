2026-09-08 22:09

Status: #baby

Tags: [[C Sharp Functions Diagnostics and Testing]] [[Test-Driven Development and Unit Test Design]]

# FIRST Test Principles

FIRST summarizes desirable automated-test properties as fast, isolated, repeatable, self-validating, and thorough. The principles keep a test suite useful as it grows by reducing shared state, manual interpretation, and long feedback delays.

The book notes that its controller test with an EF Core in-memory database satisfies many of these goals but is slower and broader than a narrow unit test. Test placement in a suite should reflect that cost and scope.

The current source presents the same qualities as fast, independent, repeatable, self-validating, and timely. Timeliness asks that the test exist when it can guide the work—immediately before production code in a test-driven cycle—while the other properties keep frequent unattended execution practical.

The current source states the same practical feedback criteria as fast, independent, repeatable, self-validating, and timely. Tests that share setup state, require a human to interpret logs, or take long enough to discourage frequent execution weaken the regression protection even when their assertions are individually correct.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
