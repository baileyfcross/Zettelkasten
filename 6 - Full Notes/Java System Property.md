2026-10-31 13:15

Status: #baby

Tags: [[Java System Runtime Services]]

# Java System Property

A Java system property is a key-value pair describing some aspect of the JVM's current runtime environment. System methods can retrieve one property or the complete property set, supply a default for a missing key, set a value, clear a key, or replace the set.

Values assigned through `System.setProperty` affect only the current runtime and disappear when the process exits. Changing a standard property after initialization may not affect code that already cached it, so runtime configuration should avoid assuming every property remains dynamically authoritative.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
