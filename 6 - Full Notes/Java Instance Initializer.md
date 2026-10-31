2026-10-31 13:15

Status: #baby

Tags: [[Java Object Construction and Class Members]]

# Java Instance Initializer

An instance field initializer assigns a field as part of constructing every object, while an instance initialization block groups construction-time statements outside a named constructor. The compiler incorporates both forms into instance initialization before the constructor body completes.

Initializers execute in their source order, making their relative placement significant when a later initializer depends on an earlier field. Constructors then add the argument-dependent work. Shared initialization in these forms can reduce repeated assignments across overloaded constructors.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
