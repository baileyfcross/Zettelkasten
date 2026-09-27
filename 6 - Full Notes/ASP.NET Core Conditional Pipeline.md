2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Conditional Pipeline

ASP.NET Core can branch its middleware pipeline according to a path or predicate. A mapped branch handles matching requests with its own component sequence, while nonmatching requests continue through the main pipeline.

Conditional branches can avoid work that is irrelevant to most requests and isolate specialized behavior. Their conditions and terminal components must remain visible, because overlapping branches or an unexpected short circuit can make route behavior difficult to trace.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
