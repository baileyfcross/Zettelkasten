2026-09-22 23:04

Status: #baby

Tags: [[Cross-Platform .NET Mobile Runtime]]

# Xamarin.Android Just-in-Time Compilation

Xamarin.Android can package managed intermediate-language assemblies together with the Mono runtime and compile methods as they execute. This just-in-time model differs from Xamarin.iOS, where runtime code generation is restricted and ahead-of-time compilation is required.

The packaged runtime forms an adaptation layer between .NET APIs and Android services. Shared code can retain its managed form while platform bindings expose Android functionality.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
