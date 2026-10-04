2026-10-04 12:25

Status: #baby

Tags: [[.NET Core Data Types and Collections]]

# Data Annotation Validation

Data annotation validation places declarative constraints on .NET types and members with attributes such as `Required`, `StringLength`, and `EmailAddress`. The annotation describes a rule in metadata, allowing a validation component to discover it through [[.NET Reflection and Attributes]].

Programmatic validation creates a `ValidationContext` and asks `Validator` to evaluate an object, collecting `ValidationResult` values for failed rules. An annotation can use a [[.NET Regular Expressions|regular-expression]] rule for structured text, but validation still has to run at the application boundary; decorating a property alone does not prove that every incoming value was checked.

# References

[[programmingincexam70-483mcsdguide.pdf]]
