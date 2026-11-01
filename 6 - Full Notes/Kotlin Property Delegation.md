2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin Property Delegation

A delegated Kotlin property uses `by` to transfer its getter and, when applicable, setter behavior to another object. The delegate implements the access protocol, allowing several properties to reuse behavior such as lazy construction, observation, or storage in another structure.

Delegation separates the property's public name and type from the mechanism that serves its accesses. The containing class can therefore adopt reusable state-management behavior without inheriting from the delegate or repeating accessor logic in every property.

# References

[[masteringkotlinforjavadevelopers.epub]]
