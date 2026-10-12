2026-09-22 23:04

Status: #baby

Tags: [[Cross-Platform .NET Mobile Runtime]]

# Xamarin.iOS Ahead-of-Time Compilation

Xamarin.iOS uses ahead-of-time compilation to turn managed application code into native machine code before the application is distributed. This accommodates iOS restrictions on generating executable code at runtime.

Because compilation happens before execution, the build must know which managed code and generic forms the application will require. The resulting application still uses Xamarin APIs, but it does not rely on a just-in-time compiler on the device.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
