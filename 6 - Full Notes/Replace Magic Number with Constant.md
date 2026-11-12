2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Replace Magic Number with Constant

Replace magic number with constant is a refactoring that gives an unexplained literal a meaningful name and one authoritative definition. The name communicates why the value exists, while the single definition prevents several uses from drifting apart when the value changes.

The transformation is appropriate when a number represents a domain rule, limit, conversion, or configuration rather than an obvious local quantity. The constant should name the concept, not merely repeat the digits in words.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

