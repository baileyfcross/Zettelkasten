2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Inner Class

A Java inner class is a non-static member class whose instances are associated with instances of the enclosing class. It can directly access that enclosing object's static and instance members, even when they are private.

External code can create one by qualifying `new` with an enclosing object, although the enclosing class commonly constructs the inner object itself. The association is useful when the nested behavior belongs to one outer object and needs its state, but it also ties the inner instance to that outer context.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
