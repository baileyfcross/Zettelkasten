2026-10-30 15:57

Status: #baby

Tags: [[Java Platform Runtime and Project Structure]]

# Java Module Directives

Module descriptors use `requires` for readable dependencies and `exports` for public packages. Qualified exports restrict a package to named consumers, while `requires transitive` makes a dependency readable to modules that depend on the declaring module. `open` and `opens` permit reflective access without exposing ordinary compile-time access.

The service directives separate an interface from its implementations: `uses` declares consumption and `provides ... with` registers a provider. Together these directives express structure that would otherwise be hidden in classpath ordering, reflection configuration, or application-specific registration code.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
