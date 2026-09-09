2026-09-08 21:16

Status: #baby

Tags: [[ASP.NET Core Page and MVC Development]]

# ASP.NET Core Action Filters

ASP.NET Core filters run at defined stages around MVC action execution and result processing. They support cross-cutting behavior such as validation checks, logging, exception policies, and response modification without repeating code in every action.

Filters can be registered globally or applied to selected controllers and actions. Their scope and order should be kept explicit because hidden control flow can make request behavior harder to understand and test.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
