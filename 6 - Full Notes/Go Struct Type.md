2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Struct Type

A Go struct groups named fields into a composite value without defining an inheritance hierarchy. Struct literals can initialize fields by position or by name, with omitted fields receiving their zero values.

Methods are declared separately with receivers rather than nested inside the struct declaration. Field order can influence alignment and memory size, and tags attached to fields provide metadata that libraries such as JSON encoders can inspect through reflection.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
