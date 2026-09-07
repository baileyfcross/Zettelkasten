2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# React useState Hook

The React `useState` hook adds one piece of local state to a function component. It returns the current value and a setter function, while its argument supplies the initial value.

Calling the setter schedules a rerender with the new state. TypeScript can infer the state type from the initial value or accept an explicit generic type when values such as `null` and loaded data are both possible.

# References

[[aspnetcore3andreact.pdf]]
