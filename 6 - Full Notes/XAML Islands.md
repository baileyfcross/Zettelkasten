2026-09-08 22:09

Status: #baby

Tags: [[Windows Desktop Modernization]]

# XAML Islands

XAML Islands allow a classic Windows Forms or WPF application to host a UWP control inside its existing desktop interface. They provide an incremental modernization path when a newer control or binding experience is useful but replacing the whole application is not justified.

The book embeds a UWP tree control in a Windows Forms screen through [[WindowsXamlHost]]. The host bridges two UI frameworks, so the application must distinguish their similarly named controls and explicitly connect the hosted control to the surrounding form.

# References

[[c8andnetcore30projectsusingazure.pdf]]
