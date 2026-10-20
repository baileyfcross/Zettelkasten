2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Context Propagation

MicroProfile Context Propagation carries container-managed context across units of work whose execution is not tied to one thread. The specification applies to abstractions such as `CompletionStage`, `CompletableFuture`, `Function`, and `Runnable` that may execute on managed threads.

Its purpose is to preserve the relevant request or application context when asynchronous work crosses thread boundaries. The code can therefore use thread-agnostic task APIs without silently losing contextual state owned by the container.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
