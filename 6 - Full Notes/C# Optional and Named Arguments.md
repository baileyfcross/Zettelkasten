2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Object-Oriented Type Design]]

# C# Optional and Named Arguments

An optional parameter declares a default value used when the caller omits that argument. Required parameters precede optional ones, making the minimum contract visible in the method signature.

A named argument associates a value with a parameter name at the call site. It improves clarity when several values share a type and can allow optional values to be supplied without listing every earlier default. Renaming a public parameter can therefore affect callers that use names.

Optional defaults must be compile-time constants and become part of how the caller is compiled. Named arguments can be combined with positional ones under the language's ordering rules, making a selective optional call readable without constructing placeholder values.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
