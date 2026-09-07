2026-09-06 20:52

Status: #baby

Tags: [[React Routing and Forms]]

# Form Context

A form context is a React context that shares field values, validation errors, touched state, and change handlers with nested form controls. It lets generic field components participate even when the form component does not reference each field directly.

The form provides the context around its children, and only descendants inside that provider can consume it. This removes prop plumbing while keeping the shared state within one form boundary.

# References

[[aspnetcore3andreact.pdf]]
