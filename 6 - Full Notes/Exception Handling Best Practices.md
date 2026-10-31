2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Exception Handling]] [[Selenium Assertions Exceptions and Test Reliability]]

# Exception Handling Best Practices

Exception handling should catch the most specific failure a layer can meaningfully address, use cleanup guarantees for dependent resources, and provide clear diagnostic messages. A custom exception is appropriate when the application needs a stable domain-specific failure contract.

Handling should happen close enough to preserve context but not so early that the code can only hide the problem. General catch blocks require an explicit fallback policy, and cleanup must run even when recovery is impossible.


For browser automation, this means catching a specific Selenium exception, using waits or a bounded retry for genuinely transient conditions, and keeping diagnostic context. An optional lookup can use `findElements()` and inspect an empty list instead of turning normal absence into an exception.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
