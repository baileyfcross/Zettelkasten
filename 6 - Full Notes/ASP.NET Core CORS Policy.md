2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]]

# ASP.NET Core CORS Policy

An ASP.NET Core CORS policy names the browser origins, HTTP methods, and headers that may make cross-origin requests to an API. The application registers the policy as a service and applies it in the middleware pipeline or to selected endpoints.

CORS is a browser access rule, not caller authentication. A permissive policy can expose responses to unintended web origins, so production policies should grant only the capabilities that known clients require.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
