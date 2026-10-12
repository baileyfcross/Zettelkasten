2026-09-27 11:11

Status: #baby

Tags: [[.NET Microservice Communication and Workers]]

# BackgroundService

`BackgroundService` is a base class for implementing long-running hosted work in .NET. A derived class places its asynchronous loop in `ExecuteAsync` and observes the supplied cancellation token so the host can coordinate a graceful shutdown.

The method represents the service's lifetime, so blocking calls and unbounded exception paths can affect the whole process. Dependencies with scoped lifetimes should be resolved through an explicit scope inside the worker operation.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
