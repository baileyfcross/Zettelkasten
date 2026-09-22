2026-09-06 20:31

Status: #baby

Tags: [[HTTP API Integration]] [[Reactive Programming in .NET]]

# Observable

An observable represents a sequence of values or events that a consumer can subscribe to over time. It fits asynchronous client behavior because the producer can emit a result, an error, or later updates without blocking the caller.

Angular [[Angular HttpClient|HttpClient]] returns observables for HTTP operations. Components and services can transform, retry, or react to those streams, and an activity log can observe form changes without repeatedly polling the form model.

.NET's `IObservable<T>` expresses the producer side of the same general idea: an observer subscribes, receives notifications as values change, and can dispose of the subscription. The inventory example makes a product recorder the provider for several reporting observers, keeping the provider independent of each report's behavior.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
