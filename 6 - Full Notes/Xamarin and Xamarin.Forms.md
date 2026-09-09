2026-09-08 21:16

Status: #baby

Tags: [[Xamarin.Forms Mobile Applications]]

# Xamarin and Xamarin.Forms

Xamarin enabled .NET applications to target iOS and Android with C# while calling each platform's native capabilities. Xamarin.Forms added a shared abstraction for common interface controls so substantial UI and application logic could be reused across mobile platforms.

Shared code does not erase platform differences. A cross-platform project still needs platform-specific startup, packaging, permissions, and integrations, with abstractions placed where behavior must diverge.

The emotion-detector project uses Xamarin.Forms as a small shared UI layer and a platform plugin for native camera access. Shared calls remain uniform, while Android and iOS packages provide separate implementations for behavior that cannot be cross-compiled directly.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
