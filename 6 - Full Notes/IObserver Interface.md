2026-09-21 22:12

Status: #baby

Tags: [[Reactive Programming in .NET]]

# IObserver Interface

`IObserver<T>` is the consumer side of .NET's observable contract. An observer receives value notifications and terminal error or completion signals from a subscribed provider. In the inventory example, product observers register with an observable recorder and react when product data changes. The subscription relationship lets the provider publish without hard-coding each consumer's behavior.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

