2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# Default Prop

A default prop supplies a component input when the consumer does not provide its optional value. It lets the common behavior remain concise while allowing a caller to override it explicitly.

For a function component, a value can be defaulted while destructuring the props parameter. The TypeScript prop remains optional to callers even though rendering receives a usable value.

In the source's React 15 patterns, `defaultProps` can be attached to class or function components, while a function component can also default a destructured parameter directly. A no-operation function is a useful default for an optional callback because the component can invoke it without branching.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
