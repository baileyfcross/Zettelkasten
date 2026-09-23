2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]] [[Xamarin Application Architecture]]

# Inversion of Control

Inversion of control moves decisions about constructing and connecting collaborators out of the component that uses them. In the book's .NET console application, a startup composition step registers interfaces and implementations, and the container supplies a user interface or inventory context when a command needs it. [[Dependency Injection]] is the usual delivery mechanism here; the broader principle is that application wiring is controlled from outside the business component.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
