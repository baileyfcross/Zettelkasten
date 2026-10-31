2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Nested Class Shadowing

Shadowing occurs when a declaration in an inner scope uses the same name as one in an enclosing scope. Inside an inner-class method, a parameter can shadow an inner field, and that field can in turn shadow a field of the enclosing class.

The unqualified name selects the nearest declaration. `this.name` selects the current inner object's field, while `OuterClass.this.name` selects the field of the associated enclosing object. These forms make each level explicit when renaming is not practical.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
