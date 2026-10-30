2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Interface Default Method

A default method gives an interface method a concrete body. Introduced with Java 8, it allows an interface to acquire behavior without immediately forcing every existing implementation to add the new method.

An implementing class inherits the default unless it overrides it. When inherited defaults conflict, the class must resolve the ambiguity explicitly. Interfaces can also declare static methods and constants, and since Java 9 they can use private instance or static helpers to share implementation internally without making those helpers part of the public contract.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
