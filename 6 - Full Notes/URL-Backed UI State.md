2026-09-30 00:32

Status: #baby

Tags: [[React Routing and Forms]]

# URL-Backed UI State

URL-backed UI state stores a presentation choice in the route when users should be able to bookmark, share, revisit, or navigate through that choice. A sort mode or selected record identifier can become a route parameter instead of a private value in the Redux store.

The URL should hold state that belongs to the site map or visible selection, not every transient application value. In the source, moving sort order into the route gives the router authority over browser-facing presentation while Redux continues to own the underlying color records.

# References

[[learningreact1.pdf]]
