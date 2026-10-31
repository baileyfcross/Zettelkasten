2026-10-31 13:15

Status: #baby

Tags: [[Java Inheritance Composition and Object Contracts]]

# Java Object String Representation

`Object.toString()` supplies a string representation that other code can request explicitly or obtain implicitly when an object is printed. Its default form combines the runtime class name with an at-sign and a hexadecimal hash-code representation.

A class can override `toString()` to expose a more useful description of its state for output and debugging. A subclass implementation may call `super.toString()` and append its own fields so the representation retains both inherited and specialized information.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
