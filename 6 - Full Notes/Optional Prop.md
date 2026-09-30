2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# Optional Prop

An optional prop is a component input that the consumer may omit. In a TypeScript props interface, the optional marker distinguishes it from inputs every use of the component must supply.

The component must define behavior for the missing value. It may render nothing for that feature, select a [[Default Prop|default value]], or derive the behavior from other inputs.

The source uses optional callback props with a default identity function. This lets the component report an event through the callback when one is supplied while remaining safe to render and interact with when the consumer omits that behavior.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
