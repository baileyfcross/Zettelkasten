2026-09-14 20:21

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]] [[Selenium Assertions Exceptions and Test Reliability]]

# False Positive

A false positive occurs when a procedure declares a feature significant even though its null hypothesis is true. It is a type I error at the level of an individual decision.

When thousands of features are tested, several false positives can occur in one experiment. Multiple-testing procedures therefore summarize or control how these errors accumulate across the entire selected set.

In classification, the same term means assigning the positive label to a case that is actually negative. Its cost is application-specific: it may be an unnecessary medical intervention or an impostor admitted by an authentication system. A decision threshold should reflect that consequence rather than minimize all errors indiscriminately.


In automated testing, a false positive is a passing result even though the application behavior is wrong. Weak assertions, swallowed exceptions, or validating only that a command ran can produce this result; the assertion must inspect the meaningful postcondition.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[machinelearning_mit.epub]]

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
