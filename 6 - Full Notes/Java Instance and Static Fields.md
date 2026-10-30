2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Instance and Static Fields

An instance field belongs to each object, so two instances can hold different values for the same declared field. A static field belongs to the class and is shared by all its instances; it can be accessed without constructing an object and is initialized when the class is initialized.

Fields receive type-specific defaults before constructor code runs. Adding `final` permits one initialization and prevents reassignment; combining `static final` is the conventional form for a class constant. A final reference cannot point to another object, but the referenced object's mutable state can still change.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
