2026-10-30 16:54

Status: #baby

Tags: [[Java Records Patterns and Construction]]

# Java Flexible Constructor Body

A flexible Java constructor body permits selected statements before an explicit `super(...)` or `this(...)` call. Arguments can be validated, normalized, or computed before the base constructor receives them, removing the need to hide every preparation step inside static helper methods.

The constructor prologue may use local variables, loops, static state, and static methods, but cannot access the not-yet-initialized instance. Base construction still occurs before subclass instance initialization, preserving the inheritance initialization order described by [[Java Constructor Overloading and Chaining]].

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
