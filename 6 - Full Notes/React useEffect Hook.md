2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# React useEffect Hook

The React `useEffect` hook performs a side effect after a function component renders. Fetching data, starting a subscription, or responding to a changed route parameter are effects because they reach beyond calculation of the returned element tree.

Its dependency array controls when the effect is repeated. An empty array runs the effect after the initial render, while listed values cause it to rerun when one changes. Cleanup can stop work when the component is removed.

# References

[[aspnetcore3andreact.pdf]]
