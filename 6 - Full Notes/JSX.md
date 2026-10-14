2026-09-06 20:52

Status: #baby

Tags: [[React Component Architecture]]

# JSX

JSX is a syntax extension that lets a React component describe element structure with HTML-like expressions inside JavaScript or TypeScript. A build step transforms JSX into ordinary JavaScript calls that create React elements.

Expressions in braces can supply values, conditions, attributes, and repeated children. JSX is not sent to the browser unchanged; it is authoring syntax for producing the [[React Element|element]] tree.

A JSX tag names the element or component type, its attributes become props, and nested tags become children. JavaScript expressions inside braces are evaluated before their values enter the tree, and Babel transpiles the complete JSX form into element-creation calls that ordinary JavaScript runtimes can execute.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
