2026-09-22 23:04

Status: #baby

Tags: [[Xamarin Application Architecture]]

# Xamarin Application Anatomy

A Xamarin application solution combines platform-agnostic code with one harness project for each target operating system. The shared portion contains reusable domain, service, and presentation logic, while each platform project supplies the native entry point, metadata, resources, permissions, and implementations that require native APIs.

Keeping those roles separate makes the sharing boundary visible. A platform-specific feature should be exposed through an interface or service rather than causing native dependencies to spread through the shared application.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
