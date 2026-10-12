2026-09-22 23:04

Status: #baby

Tags: [[Xamarin Forms Styling and Native Customization]]

# Xamarin.Forms Platform Specific

A Xamarin.Forms platform specific exposes a supported native option through the shared control API. Code can use an `On<Platform>` configuration call, and XAML can use the platform configuration namespace, to set behavior that has no identical cross-platform property.

This is lighter than writing an effect or renderer because the framework already defines the native integration. The setting affects only the target platform while the shared control remains usable elsewhere.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
