2026-09-30 00:32

Status: #baby

Tags: [[React Component Lifecycle and Integration]]

# React Mounting Lifecycle

The React mounting lifecycle covers a component's initial construction and first insertion into the rendered tree. In the source's class API, props and initial state are prepared before `render`, and `componentDidMount` runs after the DOM output exists.

Post-mount work is appropriate for a request, timer, or third-party library that needs the rendered DOM. If setup creates a continuing resource, its ownership must be paired with [[React Unmounting Lifecycle|unmount cleanup]] rather than leaving the timer, listener, or subscription active after the component disappears.

# References

[[learningreact1.pdf]]
