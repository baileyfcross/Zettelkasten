2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]]

# API Request Model

An API request model defines the fields accepted by one HTTP operation. It gives model binding and validation a transport-specific target instead of accepting a persistence entity as an unrestricted request body.

A focused request model makes writable fields explicit and can carry validation rules suited to that operation. Separate models may be appropriate when create and update requests have different requirements.

# References

[[aspnetcore3andreact.pdf]]
