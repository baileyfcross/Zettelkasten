2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Covariant Return Type

A Java overriding method may narrow a reference return type from the superclass method's type to one of its subtypes. This covariant return preserves the overriding relationship while giving callers of the subclass method a more specific result.

The narrower declaration can remove an otherwise necessary downcast. Array `clone()` uses the same principle by returning the array's own type rather than requiring callers to cast the result from `Object`.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
