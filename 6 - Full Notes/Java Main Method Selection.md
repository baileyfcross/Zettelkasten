2026-10-30 16:54

Status: #baby

Tags: [[Java Source Launch and Documentation]]

# Java Main Method Selection

Modern Java can encounter several eligible main-method forms, including static or instance methods with or without a `String[]` parameter. The simplified selection rule first chooses an eligible method with the parameter and otherwise chooses the parameterless form.

The rule makes compact programs predictable without removing the traditional entry signature. Java still rejects duplicate methods that differ only by static versus instance status, because `static` is not part of a method signature.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
