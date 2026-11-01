2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Data Class

A Kotlin data class declares its primary data in constructor properties and receives generated value-oriented operations such as `equals`, `hashCode`, `toString`, and `copy`. Component functions also support destructuring the declared properties.

The primary constructor must contain at least one `val` or `var` parameter. The generated behavior makes the declared data shape the center of the type's identity, reducing repetitive code for values that mainly carry structured information.

# References

[[masteringkotlinforjavadevelopers.epub]]
