2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Refactoring Trigger

A refactoring trigger is evidence that the current structure makes understanding or change unnecessarily difficult. The source identifies duplicated code, excessively long functions, classes with unrelated responsibilities, inconsistent abstraction in an interface, and overly long parameter lists as common signals.

The signal is a prompt to investigate rather than an automatic rule. A change is justified when it clarifies a real responsibility or removes repeated knowledge, and the resulting structure should be protected by tests that describe the behavior being preserved.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

