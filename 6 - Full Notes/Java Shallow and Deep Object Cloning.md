2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Shallow and Deep Object Cloning

Shallow cloning duplicates an object's fields but does not duplicate objects reached through its reference fields. The original and clone therefore contain distinct primitive field copies while their copied references may still point to the same nested objects.

Deep cloning also duplicates the referenced mutable objects, recursively when necessary, and installs those new references in the outer clone. Java's `Object.clone()` performs field-by-field copying for a class that implements `Cloneable`; a class seeking a deep result must add the nested cloning or reconstruction itself.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
