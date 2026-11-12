2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Assertion and Exception Boundary

The assertion and exception boundary separates violated internal assumptions from expected runtime problems. An assertion checks a condition that should never be false in a correct program and makes a programming defect immediately visible during development.

An exception represents a failure such as a missing file or invalid external input that normal operation may encounter and potentially recover from. Using an assertion for user data can terminate a production program unnecessarily, while silently catching an invariant violation can conceal a defect that should be fixed.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

