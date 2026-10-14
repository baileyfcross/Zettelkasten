2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Object Property Access

JavaScript objects store values at named properties. Dot notation, such as `obj.name`, expresses a fixed identifier directly and is usually the shorter, more readable access form.

Bracket notation, such as `obj["name"]`, accepts a string or an expression whose result supplies the property key. It is necessary when a key contains characters that are not valid in dot notation or when the key name is stored in a variable and must be chosen at runtime.

# References

[[youdontknowjs_upandgoing.pdf]]
