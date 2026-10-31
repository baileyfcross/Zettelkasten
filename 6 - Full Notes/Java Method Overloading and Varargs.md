2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]] · [[Java Object Construction and Class Members]]

# Java Method Overloading and Varargs

Method overloading declares several methods with the same name but different parameter lists. The compiler chooses an applicable overload from the argument types and conversions at the call site; changing only the return type does not create a distinct overload.

A variable-arity parameter, written with `...`, lets callers supply zero or more values that the method receives as an array. It must be the last parameter. Varargs are useful for entry points and convenience APIs, but an ordinary array parameter can be clearer when the caller already owns a collection of values.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
