2026-09-22 20:53

Status: #baby

Tags: [[Domain Model Building Blocks]]

# Value Object

A value object represents a domain concept defined by its values rather than by a continuing identity. It gives primitive data an explicit type in the [[Ubiquitous Language]], controls how valid instances are created, and can define meaningful operations over those values. A price, title, or user identifier can reject invalid input before it reaches a [[Domain Entity]]. Value objects are preferably immutable, so replacing one value does not create hidden changes elsewhere.

# References

[[hands-ondomain-drivendesignwithnetcore.pdf]]
