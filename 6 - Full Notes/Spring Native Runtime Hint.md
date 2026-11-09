2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Native Runtime Hint

A Spring native runtime hint tells the AOT process which reflection, resources, serialization, proxies, or JNI behavior must remain available in a GraalVM native image. The hint fills gaps that static analysis cannot infer, especially when a third-party library discovers types dynamically.

Spring's AOT engine generates many hints from the application context, dependency injection, conditions, and known framework annotations. A custom hint should describe only the dynamic behavior actually required, because broad reflection registration increases image size and weakens closed-world optimization. Native tests are the evidence that an overlooked path has not been removed.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
