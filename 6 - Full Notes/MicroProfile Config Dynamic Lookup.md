2026-11-08 14:08

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Config Dynamic Lookup

MicroProfile Config can resolve a property again each time application code asks for it. Injecting a Provider or Supplier and calling get retrieves the latest value from the underlying configuration sources, unlike a value captured once through ordinary direct injection.

A missing dynamically retrieved property raises a runtime exception when the provider or supplier returns a plain type. Wrapping the target in Optional combines current-value lookup with explicit absence handling. The Config API also offers direct getValue and getOptionalValue calls, while ConfigValue exposes metadata such as the winning source name, ordinal, raw value, property name, and converted value.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
