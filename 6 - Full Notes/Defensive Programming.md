2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Defensive Programming

Defensive programming anticipates invalid input, failed operations, null references, incorrect sizes or types, zero denominators, and out-of-range values at the boundaries where they can enter a program. Checks make assumptions explicit so a bad value is handled near its source instead of corrupting distant state.

The response depends on whether the condition is expected and recoverable. Validation and exceptions can report ordinary runtime failures, while an assertion is reserved for an internal condition that should be impossible if the program is correct.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

