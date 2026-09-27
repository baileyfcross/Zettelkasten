2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Filter Pipeline

The ASP.NET Core MVC filter pipeline surrounds selected stages of controller processing, including authorization, resource handling, action execution, exception handling, and result execution. A filter can observe or replace behavior at the stage its interface represents.

Filters operate inside MVC after general middleware has routed the request to that framework. Cross-cutting behavior belongs at the narrowest layer that provides the context it needs and covers the intended endpoints.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
