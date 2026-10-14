2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# Function Component

A function component is a JavaScript or TypeScript function that accepts props and returns React elements. It provides a reusable piece of interface without requiring a component class.

Hooks such as [[React useState Hook|useState]] and [[React useEffect Hook|useEffect]] give function components local state and lifecycle-related effects. A TypeScript function-component type can associate a defined props interface with the function.

The source calls the historical state-free form a stateless functional component: a function receives props and returns elements without an instance `this`. Destructuring can expose the required props at the parameter boundary, and keeping the function pure makes its UI output straightforward to test.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
