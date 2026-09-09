2026-09-08 21:16

Status: #baby

Tags: [[Xamarin.Forms Mobile Applications]]

# Xamarin.Forms Two-Way Data Binding

Two-way binding copies a source value into a control and sends user edits from the control back to the source. It is useful for interactive properties such as text fields and switches where interface state and view-model state must remain synchronized.

The binding mode should match the actual flow of ownership because unnecessary two-way updates make behavior harder to trace. Validation and conversion are still required when user-entered values cross into application state.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
