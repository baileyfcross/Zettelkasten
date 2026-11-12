2026-11-11 18:27

Status: #baby

Tags: [[Software Construction and Refactoring]]

# Intent-Revealing Identifier

An intent-revealing identifier tells a reader what a value, operation, or type means in its context. A descriptive name such as `interestRate` preserves knowledge that an abbreviation may lose after the author or surrounding code changes.

Names should be specific without becoming sentences, and a codebase should use the same term for the same concept. Renaming is a behavior-preserving improvement when the old name hides purpose, and it reduces the need for comments that merely translate an obscure identifier.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

