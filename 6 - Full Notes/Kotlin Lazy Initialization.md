2026-10-31 13:27

Status: #baby

Tags: [[Kotlin Functions Null Safety and Delegation]]

# Kotlin Lazy Initialization

Kotlin's `lazy` delegate defers computing a read-only property's value until the property is first accessed. The initialization lambda supplies the value, which is then retained for later reads instead of being recomputed each time.

Lazy initialization avoids work for a value that may never be needed and moves construction closer to first use. That timing also matters: any cost or failure in the initializer occurs on access rather than at the containing object's ordinary construction point.

# References

[[masteringkotlinforjavadevelopers.epub]]
