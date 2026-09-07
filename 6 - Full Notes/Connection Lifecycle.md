2026-09-06 20:52

Status: #baby

Tags: [[Real-Time Web Communication]]

# Connection Lifecycle

A connection lifecycle is the sequence from creating and starting a real-time connection through receiving messages and eventually stopping it. Each stage can complete asynchronously or fail independently.

In a React component, an effect can start the connection after rendering and return cleanup that stops it when the component is removed. This keeps network resources aligned with the feature that owns them.

# References

[[aspnetcore3andreact.pdf]]
