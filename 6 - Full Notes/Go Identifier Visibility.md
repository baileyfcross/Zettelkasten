2026-10-19 01:48

Status: #baby

Tags: [[Go Program Structure and Toolchain]]

# Go Identifier Visibility

Go determines package visibility from the first letter of an identifier. A name beginning with an uppercase Unicode letter is exported and can be addressed by importing packages; a lowercase initial keeps it accessible only within its package.

This rule applies to top-level declarations and to fields or methods exposed through a type. Go does not provide Java's public, protected, package-private, and private modifier set, so package boundaries and smaller interfaces carry more of the encapsulation responsibility.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
