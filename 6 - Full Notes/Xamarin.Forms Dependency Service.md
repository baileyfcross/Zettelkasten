2026-09-08 21:16

Status: #baby

Tags: [[Xamarin.Forms Mobile Applications]]

# Xamarin.Forms Dependency Service

The Xamarin.Forms dependency service allows shared code to request an interface whose implementation is supplied by each platform project. It provides a bridge for capabilities that cannot be expressed through the common Xamarin.Forms API.

Shared code depends on the abstraction rather than Android or iOS classes, preserving portability at the call site. Platform implementations must be registered and should keep the platform-specific surface as narrow as the required capability permits.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
