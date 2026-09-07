2026-09-06 20:43

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# Endpoint Routing

Endpoint routing matches an incoming [[HTTP Request]] to a declared application endpoint. ASP.NET Core adds routing middleware to the request pipeline and maps patterns to controller actions, Razor Pages, or other handlers.

The endpoint middleware runs after earlier components such as static-file handling. Its position therefore determines whether a request reaches an [[MVC Controller]], a [[Razor Pages|Razor Page]], or continues to a later single-page-application fallback.

# References

[[aspnetcore3andangular9_3ed.pdf]]
