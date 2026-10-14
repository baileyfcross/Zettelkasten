2026-09-30 00:32

Status: #baby

Tags: [[React Component Lifecycle and Integration]]

# Higher-Order Component

A higher-order component is a function that receives a component and returns a new component that supplies reusable behavior through props. The wrapper can own state or lifecycle integration while the injected component remains concerned with how the received values and callbacks are displayed.

The source uses this pattern to reuse data-loading and expand-collapse behavior across different presentation components. Because the wrapper should pass through unrelated props, the composed component can retain its original contract while gaining the additional state and operations.

# References

[[learningreact1.pdf]]
