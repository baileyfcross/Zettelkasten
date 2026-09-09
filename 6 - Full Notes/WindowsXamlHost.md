2026-09-08 22:09

Status: #baby

Tags: [[Windows Desktop Modernization]]

# WindowsXamlHost

`WindowsXamlHost` is the wrapper used by XAML Islands to place a UWP control inside a Windows Forms application. Its initial type name identifies the UWP control to create, and the host itself is positioned and added like another control on the form.

The host's child-changed event gives the application access to the created UWP child so its data source and template can be configured. This separates the inter-framework bridge from the [[UWP TreeView Control]] that supplies the actual interface behavior.

# References

[[c8andnetcore30projectsusingazure.pdf]]
