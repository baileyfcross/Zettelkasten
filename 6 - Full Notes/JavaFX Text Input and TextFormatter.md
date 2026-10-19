2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Controls and Styling]]

# JavaFX Text Input and TextFormatter

`TextField` accepts single-line input, `TextArea` accepts multiple lines, and `PasswordField` masks sensitive input while disabling cut and copy. These controls handle plain text; JavaFX uses `HTMLEditor` when rich HTML-formatted content is required.

A `TextFormatter` can filter and modify proposed edits before they reach a text control. It can also pair a displayed representation with a typed value through a converter, allowing a field to expose an integer or another value type rather than only raw text. A filter may be used without a converter, but a formatter without a converter cannot accept a separately assigned typed value. Formatter state can participate in [[JavaFX Property Binding]] so validation affects other controls immediately.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
