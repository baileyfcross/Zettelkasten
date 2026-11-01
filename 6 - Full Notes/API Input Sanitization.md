2026-10-31 21:16

Status: #baby

Tags: [[REST API Security and Access Control]]

# API Input Sanitization

API input sanitization removes, escapes, or normalizes content that would be unsafe in the context where it will later be used. The book illustrates stripping dangerous HTML from comments and using parameterized database queries instead of constructing commands from request strings.

Sanitization is context-dependent and does not replace validation. A value can satisfy its data shape yet remain dangerous when interpreted as HTML, SQL, a path, or another executable language; the safe transformation must match that eventual sink.

# References

[[masteringrestapis.epub]]
