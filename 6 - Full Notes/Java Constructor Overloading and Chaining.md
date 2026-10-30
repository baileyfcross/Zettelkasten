2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Constructor Overloading and Chaining

A constructor initializes a new object and has the class name with no return type. A class can overload constructors to accept different initialization data; when no constructor is declared, the compiler can supply a no-argument constructor, but declaring any constructor removes that implicit default.

Constructor chaining centralizes initialization. `this(...)` delegates to another constructor in the same class, while `super(...)` invokes a superclass constructor; either call must be the constructor's first statement. Chaining avoids duplicating field assignments and ensures superclass state is established before subclass initialization completes.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
