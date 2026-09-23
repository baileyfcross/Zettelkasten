2026-09-22 23:04

Status: #baby

Tags: [[Xamarin Application Architecture]]

# Mobile Presentation Architecture

A mobile presentation architecture assigns responsibility for interface rendering, user actions, view state, and domain operations to distinct components. Xamarin applications commonly use Model-View-Controller or Model-View-ViewModel so pages do not become the sole location for navigation, validation, service calls, and state changes.

The appropriate pattern depends on the UI framework and binding support. Its value comes from creating testable boundaries and a predictable direction of communication, not merely from naming classes after pattern roles.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
