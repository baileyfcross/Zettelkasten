2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Selenium Cleanup with Finally

Selenium cleanup with `finally` releases browser resources whether the protected test steps succeed or raise an exception. Placing `driver.quit()` or another teardown operation in the final block prevents an abnormal path from leaving a live session behind.

The final block complements targeted catch clauses: catches decide how a failure is interpreted, while `finally` performs cleanup that must occur regardless of that interpretation.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
