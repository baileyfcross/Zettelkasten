2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Connected Component

A connected component is a React component associated with selected Redux state and dispatchable operations. Mapping functions translate the store's broad interface into the specific props that the component requires.

This boundary separates presentation from shared-state wiring. A component can render ordinary props while the connection layer subscribes to relevant store changes and wraps action creators for dispatch.

# References

[[aspnetcore3andreact.pdf]]
