2026-09-30 00:32

Status: #baby

Tags: [[React Component Architecture]]

# React Component Property Validation

React component property validation declares the expected type or custom constraint for incoming props and reports mismatches during development. A required marker distinguishes an omitted input from an optional one, while a custom validator can inspect value-specific rules such as a title's type and length.

The source uses the React 15-era `PropTypes` API and places declarations on class or function component objects. Validation does not transform a value or supply it; [[Default Prop|default props]] handle absence, while validation makes an invalid component contract visible as a warning.

# References

[[learningreact1.pdf]]
