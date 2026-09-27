2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Route Constraint

An ASP.NET Core route constraint limits a parameter match according to a rule such as value type or a custom condition. It helps routing choose among otherwise similar templates before the selected endpoint executes.

A custom constraint implements the matching contract and should answer only whether the route value belongs to that route. Input validation still belongs after selection, because using constraints to report all invalid data can turn a clear client error into an unexplained route miss.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
