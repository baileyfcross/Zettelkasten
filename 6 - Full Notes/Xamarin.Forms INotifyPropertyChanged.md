2026-09-08 21:16

Status: #baby

Tags: [[Xamarin.Forms Mobile Applications]]

# Xamarin.Forms INotifyPropertyChanged

`INotifyPropertyChanged` lets a bound object announce that one of its property values changed. Xamarin.Forms listens for the notification and refreshes targets whose bindings depend on the named property.

A view model normally raises the event only after a value actually changes and uses a consistent setter pattern to avoid omissions. Dependent calculated properties may require their own notifications when a source property changes.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
