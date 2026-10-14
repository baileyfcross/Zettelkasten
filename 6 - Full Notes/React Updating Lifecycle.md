2026-09-30 00:32

Status: #baby

Tags: [[React Component Lifecycle and Integration]]

# React Updating Lifecycle

The React updating lifecycle runs when component state changes or a parent supplies new props. It surrounds the next render with opportunities to compare old and new inputs, decide whether an update is necessary, and interact with the DOM after the update has been applied.

In the source's React 15 API, `shouldComponentUpdate` acts as a performance gate: returning false skips the component and its descendant updates when relevant values have not changed. Calling state updates indiscriminately from update callbacks can create a recursive loop, so the lifecycle must not be treated as a general mutation hook.

# References

[[learningreact1.pdf]]
