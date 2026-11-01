2026-10-31 21:16

Status: #baby

Tags: [[REST Framework and Serverless Implementations]]

# Laravel Eloquent and Fractal Serialization

Laravel can serialize Eloquent model results directly into JSON for an API response. When the public shape should differ from the model, the book uses a Fractal transformer to select and restructure the returned fields.

Direct serialization is concise but can couple consumers to persistence details. A transformation layer creates a named place for output policy, related-resource presentation, and version-specific changes while Eloquent remains responsible for database interaction.

# References

[[masteringrestapis.epub]]
