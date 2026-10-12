2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Web API Development]]

# ASP.NET Core ApiController Attribute

The ASP.NET Core `ApiController` attribute marks a controller as an HTTP API boundary and enables API-oriented conventions. It infers common binding sources for parameters and automatically turns invalid model state into an error response.

It is commonly paired with `ControllerBase`, which supplies HTTP action-result helpers without view rendering. The conventions reduce repeated transport code but make the framework's inferred behavior part of the controller contract.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
