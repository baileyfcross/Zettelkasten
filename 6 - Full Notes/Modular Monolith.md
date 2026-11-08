2026-11-06 13:52

Status: #baby

Tags: [[Microservice Architecture Adoption]]

# Modular Monolith

A modular monolith separates related functionality into modules, layers, or packages while deploying the application as one unit. Its module boundaries organize source code and team work, but its runtime boundary still encloses every module, so selective deployment and scaling stop at the application boundary.

That distinction explains why internal modularity does not automatically provide microservice autonomy. Synchronous in-process dependencies, a shared technology baseline, and one deployment can keep logically separate modules operationally coupled. A modular monolith can still be a deliberate starting point, but extracting a module should be driven by a need for independent deployment, scaling, or ownership rather than by the existence of a package boundary alone. See [[Monolithic Application Trade-Off]] and [[Thoughtful Monolith-to-Microservices Migration]].

The architecture should be selected against the system's actual constraints. A monolith can minimize distributed operations, a modular monolith can enforce stronger internal boundaries while retaining one deployment, and microservices can add independent release and scaling at the cost of network, data, security, and observability coordination. The modular form is therefore an option in its own right, not only an unfinished microservice system.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
