2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]] [[Angular Application Architecture]] [[ASP.NET Core Page and MVC Development]] [[.NET Dependency Injection and Service Lifetimes]]

# Dependency Injection

Dependency injection supplies an object with its collaborators instead of making it construct or locate them itself. This reduces hard-coded dependencies and supports reuse, readability, configuration, and isolated testing.

ASP.NET Core registers application services during startup and injects them into consumers such as controllers. Angular applies the same design principle to components and services, allowing an [[Angular HttpClient]] or a custom [[Data Service]] to be supplied through a constructor.

In the inventory application, commands depend on read or write context interfaces and the .NET service provider supplies their implementations through constructor injection. Registration also specifies whether an instance is transient, scoped, or shared as a singleton; this construction policy is distinct from the business behavior of the command.

Its .NET examples register abstractions and implementations with the generic host or ASP.NET Core service collection, moving object composition and lifetime selection away from business behavior that consumes the dependency.

Go applies the same design without requiring a standard container: a constructor function can accept small interfaces for collaborators such as logging, caching, database access, or HTTP calls. Explicit assembly in `main` keeps the object graph visible, while reflection- or code-generation-based containers become options when manual wiring grows too complex.

Helidon makes the choice visible at the programming-model boundary. Helidon MP uses Jakarta CDI annotations such as `@Inject` and `@ApplicationScoped` to construct and scope managed beans, while Helidon SE deliberately omits a dependency-injection container and assembles services through explicit builders and constructors.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
