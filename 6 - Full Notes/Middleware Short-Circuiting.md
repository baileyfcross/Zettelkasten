2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# Middleware Short-Circuiting

Middleware short-circuits the request pipeline when it produces a complete response without invoking the next component. Static content, rejected authentication, cached output, or a terminal endpoint can therefore prevent unnecessary later work.

Short-circuit behavior depends on registration order. A component that ends the pipeline too early can bypass routing, authorization, logging, or other behavior that the application expected to run.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
