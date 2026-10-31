2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# TestNG Test Dependency

A TestNG test dependency uses `dependsOnMethods` or a related dependency declaration to require another test or group to succeed first. If the prerequisite fails, the dependent test is skipped rather than executed in an invalid state.

Dependencies can represent a necessary workflow but also make results order-sensitive. Independent tests are easier to run and diagnose, so dependency should be used only when the relationship is intrinsic.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
