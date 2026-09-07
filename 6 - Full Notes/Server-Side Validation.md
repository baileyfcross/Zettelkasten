2026-09-06 20:34

Status: #baby

Tags: [[Web Forms and Validation]]

# Server-Side Validation

Server-side validation checks submitted values inside the trusted application boundary before data is accepted or changed. It protects rules even when the client omits, alters, or bypasses its own checks.

The server should return a meaningful [[HTTP Status Code]] and validation result that the Angular form can present. A uniqueness rule can also be exposed as a narrow API used by an [[Asynchronous Validator]].

# References

[[aspnetcore3andangular9_3ed.pdf]]
