2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Access Control Levels

Java member access has four levels. `public` is visible everywhere; `protected` is visible in the declaring package and to subclasses; an omitted modifier gives package-private access; and `private` restricts access to the declaring class. Top-level types can be public or package-private.

An access modifier states which code may name a member, not whether that member is safe or appropriate to use. [[Java Encapsulation with Accessors]] combines restricted fields with deliberate methods, while module exports add a coarser boundary that can prevent another module from accessing even public types in an unexported package.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
