2026-11-11 18:27

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]]

# Branch Coverage

Branch coverage checks whether tests exercise each outcome of a decision. An `if` condition needs evidence for both true and false paths, a `switch` needs each case and its default, and compound Boolean expressions may require cases that expose short-circuit evaluation.

The metric directs attention to control-flow alternatives but does not choose meaningful values by itself. A test can enter a branch with an unrepresentative input, so branch evidence should be paired with [[Data Coverage]] and explicit expected results.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

