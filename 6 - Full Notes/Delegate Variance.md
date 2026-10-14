2026-10-04 12:25

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# Delegate Variance

Delegate variance allows a method to satisfy a compatible delegate signature even when the reference types are not identical. Covariance permits the method to return a more derived type than the delegate declares, while contravariance permits it to accept a less derived parameter type.

These rules let C# delegates reuse methods without adapter wrappers while retaining compile-time type safety. A method returning a [[Derived Class]] can stand in for one returning its [[Base Class]], and a method that accepts the base can handle calls made through a delegate whose parameter is the derived type.

# References

[[programmingincexam70-483mcsdguide.pdf]]
