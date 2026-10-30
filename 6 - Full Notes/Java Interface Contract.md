2026-10-30 15:57

Status: #baby

Tags: [[Java Classes Interfaces and Type Declarations]]

# Java Interface Contract

A Java interface defines behavior that implementing classes agree to provide. Its abstract methods are implicitly public, and a nonabstract implementing class must supply concrete implementations. One class can implement several interfaces, and an interface can extend multiple interfaces.

The contract decouples a caller from a particular implementation and supports polymorphism without sharing instance fields or constructor logic. Modern interfaces may also contain constants, static methods, default methods, and private helpers, but their central role remains to name an externally usable capability rather than an object's stored representation.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
