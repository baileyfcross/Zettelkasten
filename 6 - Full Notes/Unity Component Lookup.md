2026-09-28 22:14

Status: #baby

Tags: [[Unity Game Development]]

# Unity Component Lookup

Unity component lookup retrieves a component of a requested type from a GameObject, allowing one behavior to use the data or services supplied by another. The same mechanism works for built-in components such as renderers and colliders and for custom MonoBehaviour classes.

Lookup makes composition usable but creates a dependency that should be checked and, when repeatedly accessed, cached. A missing component is a configuration error unless absence is explicitly supported. Requirements are easier to maintain when the script's expected collaborators are visible in its design rather than discovered only after a null reference at runtime.

# References

[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

