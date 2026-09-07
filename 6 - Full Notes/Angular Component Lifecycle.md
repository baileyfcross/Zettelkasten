2026-09-06 20:31

Status: #baby

Tags: [[Angular Application Architecture]]

# Angular Component Lifecycle

The Angular component lifecycle is the sequence of creation, initialization, change handling, and destruction events through which a component passes. Lifecycle hooks let application code respond at defined stages rather than relying on arbitrary timing.

`ngOnInit` is commonly used for initialization after Angular has constructed the component and supplied its dependencies. A component can use that hook to begin an [[Angular HttpClient]] request or subscribe to an [[Observable]].

# References

[[aspnetcore3andangular9_3ed.pdf]]
