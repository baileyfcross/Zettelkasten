2026-09-06 20:52

Status: #baby

Tags: [[Redux State Management]]

# Redux Provider

A Redux provider places the store into React's component context so descendants can access it without passing the store through every intermediate prop. It normally wraps the application near the root of the component tree.

The provider supplies access, while connected components or hooks choose which state and dispatch operations they consume. This keeps the store shared without making every component depend on its entire contents.

In the source's React Redux API, the provider wraps one root child and publishes the supplied store through context. It also causes the wrapped application to update after dispatch, while `connect` creates the narrower containers that map store state and operations into component props.

# References

[[aspnetcore3andreact.pdf]]

[[learningreact1.pdf]]
