2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# React Element

A React element is an object describing what should appear at one position in the interface tree. JSX expressions produce these element descriptions for intrinsic browser elements or for other React components.

Elements are descriptions rather than mutable document nodes. React compares the newly produced tree with the prior rendering and applies the required browser updates.

`React.createElement` records an element type, a props object, and its children. The resulting JavaScript object contains the instructions used to construct browser output; nested child elements form the [[Virtual DOM|virtual element tree]] rooted at the element sent to the renderer.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
