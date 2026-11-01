2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Object-Oriented Type Design]]

# Kotlin Sealed Class

A sealed Kotlin class defines a bounded inheritance hierarchy whose permitted direct forms are known to the compiler. It is abstract in use: programs construct one of its concrete subclasses rather than the sealed base itself.

Because the family is closed and knowable, a `when` expression can distinguish the subclasses exhaustively without a generic fallback when every case is covered. A sealed hierarchy is therefore suited to a value that has several distinct shapes but should not be extended arbitrarily elsewhere.

# References

[[masteringkotlinforjavadevelopers.epub]]
