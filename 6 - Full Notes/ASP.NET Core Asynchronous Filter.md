2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Asynchronous Filter

An asynchronous MVC filter awaits the next stage and can run logic before and after it without synchronously blocking a request thread during I/O. Its context exposes the action, result, exception, or resource information appropriate to the filter type.

The filter must call or deliberately replace the continuation exactly according to its policy. Mixing synchronous blocking with asynchronous actions can reduce service throughput and obscure where failures are observed.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
