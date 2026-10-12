2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Exception Filter

An ASP.NET Core exception filter observes an unhandled exception raised during MVC action processing and can replace it with a controlled action result. It centralizes transport-level error formatting for selected controllers or actions.

The filter should log safe diagnostic context and return a stable client contract without exposing implementation details. Exceptions raised outside MVC or before action execution may require middleware because they never reach this filter stage.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
