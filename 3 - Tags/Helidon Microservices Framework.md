# Helidon Microservices Framework

Parent topic: [[Microservice Engineering]]

## Overview Chapter

Helidon is an open-source Java framework and library collection for building microservices. Its architecture is deliberately divided between two programming models that share a runtime but expose different design choices. Helidon SE is a compact functional API whose application explicitly assembles configuration, routes, handlers, clients, data access, and security. Helidon MP is a declarative MicroProfile runtime in which annotations and Jakarta CDI manage resources and cross-cutting behavior. Both models produce standalone Java applications rather than artifacts that must be deployed into a separate application server.

### Programming models and a common runtime

[[Helidon Platform Models and Project Tooling]] begins with the choice between SE and MP. SE omits annotations, dependency injection, and enterprise-Java standards in favor of explicit builders and functional handlers. MP uses annotations heavily, injects managed components, supports MicroProfile, and supplies part of Jakarta EE. The difference is visible even in a greeting service: SE registers an `HttpService` and handler functions, while MP marks a resource with path, scope, HTTP-method, and configuration annotations. This is not a distinction between a standalone service and an application server; both are executable applications running in their own JVM.

The shared runtime changed significantly in Helidon 4. Versions 1 through 3 placed reactive SE and MP components over a Netty-based asynchronous server. Helidon 4 replaced that layer with Helidon Níma, a ground-up server based on Java virtual threads, and established JDK 21 as the minimum version for that release train. The public programming model becomes blocking and synchronous while the runtime uses lightweight virtual threads to serve concurrent work.

Several generation paths produce the same essential project. Maven Quickstart archetypes create an SE or MP greeting service with sources, tests, configuration, logging, Dockerfiles, and Kubernetes configuration. The Helidon CLI adds guided choices for release, model, application type, JSON library, and project coordinates, plus a development loop that recompiles and restarts after source changes. Project Starter provides those choices through a web interface and returns a ZIP. Generated projects can run as ordinary JARs, use `jlink` to create a tailored Java runtime image, or use GraalVM Native Image to build a native executable.

### Standards define the MP contract

[[MicroProfile and Jakarta Standards]] supplies the portability contract behind Helidon MP. MicroProfile began as a vendor and community effort to adapt enterprise Java to microservice architectures. Its original minimum combined CDI, JSON Processing, and RESTful Web Services; later specifications added external configuration, fault tolerance, metrics, health, JWT propagation, OpenAPI, REST clients, messaging, context propagation, GraphQL, long-running actions, and telemetry. A runtime earns compatible status by passing the specification Technology Compatibility Kit and obtaining approval for its compatibility request, which distinguishes an interoperable implementation from a similar proprietary API.

MicroProfile Config injects environment-dependent settings without rebuilding an application. OpenAPI automatically exposes a service description at `/openapi`, and Rest Client provides a type-safe HTTP invocation model. Reactive Messaging connects event-driven services, while Context Propagation carries container context across thread-agnostic units such as completion stages and runnables. The specification set changes over time: Open Tracing moved to stand-alone status after the OpenTelemetry convergence, and Metrics later became stand-alone when vendors differed over the preferred measurement API.

Jakarta EE supplies many of the underlying enterprise contracts. Platform and Web profiles cover broad and web-focused deployments, while the Core Profile selects a smaller set for cloud-native runtimes and ahead-of-time compilation. Jakarta EE 9 also replaced the `javax` package namespace with `jakarta` across the platform. Helidon MP therefore combines a particular generation of MicroProfile with compatible Jakarta APIs; project dependencies and imports must agree on those versions rather than mixing namespaces arbitrarily.

### HTTP services and clients

[[Helidon WebServer and WebClient]] is the operational center of an SE service. WebServer is built from an immutable configuration prototype that describes listeners and routings. A program can set the port and handlers directly or load listener settings from the `server` subtree of external configuration. A port of zero requests an available ephemeral socket, allowing a test or paired client to discover the chosen port after startup.

Routing binds an HTTP method and path rule to one or more handlers. Individual lambdas can serve a compact endpoint, while an `HttpService` groups relative routes beneath a registered prefix. The greeting example mounts a service at `/greet`; within it, GET handlers serve a default or named greeting and a PUT handler updates the salutation. Named path segments such as `/{name}` are obtained through the request's path-parameter view, and the response can carry text, a JSON object, or an explicit status such as 204 or 400.

WebClient performs the outbound side of the exchange. Its builder combines a base URI, connection and read timeouts, redirect limits, cookie and header behavior, external configuration, and optional client services. The client can submit a JSON entity with PUT, request a response directly as text or JSON, follow a redirect, or stream a response entity into a file. Opening the lower-level response makes the caller responsible for closing it. A metrics service can be attached to selected HTTP methods so calls increment a named counter without modifying each request method.

### Configuration is a processing pipeline

[[Helidon Configuration System]] turns files and runtime inputs into one immutable tree. Sources can come from environment variables, system properties, classpath resources, files, directories, URLs, or in-memory objects. Parsers transform properties, YAML, JSON, or HOCON bytes into the node model; mappers convert subtrees into Java types; filters transform elementary values; overrides replace selected keys; and token references let one value depend on another. Java service loading can discover parsers, mappers, filters, and overrides, while builders can disable that automatic registration.

Source behavior is also explicit. Eager sources provide a complete stream or object tree, while a lazy source resolves one key at a time. Mutable sources may expose a pollable signature, a watcher, or direct change events. A directory source turns filenames into keys and file contents into values, which the example uses for separate credential files. Ordered source merging combines developer overrides, deployment configuration, and classpath defaults, and meta-configuration can itself identify the sources to load. Filter caching determines whether a transformation runs once per key or every time the value is read.

### Data access through a configured abstraction

[[Helidon Database Client]] presents relational JDBC and MongoDB behind a common SE API. MongoDB uses a native reactive driver, while JDBC work is wrapped by an executor so the blocking driver can participate in the client's reactive flow. Backpressure lets a query subscriber request result data at its own pace rather than receiving an unbounded result set.

The database type, connection details, and native statements live in configuration. Application code invokes stable names such as `select-all` or `delete-all`, while one environment can supply SQL and another can supply a MongoDB JSON operation. The abstraction does not erase database-specific syntax; it moves that syntax outside the service code. Client services intercept statement execution to add counters, timers, health checks, and traces. Named statements improve this instrumentation because each operation has a stable semantic identity.

### Security at the route boundary

[[Helidon Security Integration]] bootstraps authentication, authorization, auditing, and outbound security through a provider model. Providers include HTTP Basic and Digest authentication, HTTP signatures, attribute-based access control, JWT, header assertion, OpenID Connect, and external identity integrations. Security can be built programmatically, loaded from configuration, or assembled with a hybrid of the two.

WebServer configuration establishes a default authentication posture and then applies path-specific rules. A rule can select HTTP methods, require one or more roles, permit optional authentication, or enable audit. Optional authentication suppresses a challenge but does not grant a required role. In the HTTP Basic example, configured users have credentials and role arrays; a user with no roles can authenticate but cannot enter role-protected paths. After evaluation, the request context exposes a security context containing the resolved user and roles so the handler can inspect identity without parsing provider credentials itself.

### Measurements, failure policies, and health

[[Helidon Metrics Instrumentation]] implements the MicroProfile Metrics model. Separate base, vendor, application, and custom scopes organize registries and endpoints. Base measurements describe JVM and operating-system conditions such as heap use, garbage collection, uptime, threads, loaded classes, processors, and CPU behavior. Application measurements can be registered through the API, generated from annotated CDI beans, or enabled for REST requests.

`@Counted` increments invocation counts, `@Gauge` reports a current numeric value, and `@Timed` records invocation frequency and duration. Programmatic histograms collect observations and expose count, sum, maximum, and quantiles. Metadata supplies names, descriptions, units, scopes, and tags. The endpoints use Prometheus text format, in which `HELP` and `TYPE` lines describe a measurement and labeled sample lines carry values.

[[Helidon Fault Tolerance and Health]] completes the operational model. Retry repeats selected failures with limits, delays, exception rules, and optional jitter. Timeout bounds execution time. Circuit breaker observes a rolling request window and moves among closed, open, and half-open states. Bulkhead caps concurrent calls and, for asynchronous invocations, can use a bounded waiting queue. Fallback redirects a qualifying failure to a compatible handler, while asynchronous execution returns a future or completion stage rather than blocking the caller.

Health answers different lifecycle questions. `/health/live` reports whether an instance should continue or be replaced; `/health/ready` reports whether it can currently perform its task; and `/health/started` reports whether initialization has advanced enough for the other checks to matter. Custom CDI beans implement `HealthCheck`, use the appropriate annotation, and return named `UP` or `DOWN` responses with optional diagnostic data. GET requests return detailed JSON, HEAD requests return status only, and HTTP success or service-unavailable codes let infrastructure act without interpreting business output.

Taken together, these parts form one framework rather than unrelated libraries. The programming model selects explicit SE composition or standards-based MP declaration. The virtual-thread runtime hosts both. Configuration feeds listeners, clients, database implementations, and security policy; routing connects requests to services; provider and interceptor boundaries attach identity and observability; and metrics, failure policies, and health endpoints make runtime behavior visible and controllable. Helidon's central tradeoff is therefore not between convenience and engineering discipline, but between two explicit ways of expressing the same microservice lifecycle on a shared Java foundation.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Helidon Microservices Framework]]"
```
