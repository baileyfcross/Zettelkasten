2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# TestNG Expected Exception

A TestNG expected-exception declaration states that a test passes only if it throws a specified exception type. The `expectedExceptions` attribute on `@Test` turns the failure path itself into the behavior under examination.

The expected type should be specific enough to reject unrelated failures. If no exception or a different exception occurs, the test must fail rather than accepting any abnormal termination.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
