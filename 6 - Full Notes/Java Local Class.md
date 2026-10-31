2026-10-31 13:15

Status: #baby

Tags: [[Java Nested Types and Package Organization]]

# Java Local Class

A local class is declared inside a block such as a method body. Its name and declaration are visible only within that block, placing a helper implementation close to the operation that uses it.

The class can use members of its enclosing class and can capture local variables or parameters that are final or effectively final. A method can instantiate the local class and return it through a superclass or interface type, keeping the concrete implementation private to the method.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
