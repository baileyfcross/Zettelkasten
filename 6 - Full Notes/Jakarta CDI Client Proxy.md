2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Client Proxy

For a normal-scoped Jakarta CDI bean, an injected reference is generally a container-generated client proxy rather than a direct reference to one contextual instance. When a method is invoked, the proxy identifies the active context, obtains the correct instance for that context, and delegates the call.

This indirection lets a long-lived component refer safely to a shorter-lived dependency because the concrete target can change from request to request. It also enables lazy creation and helps the container handle circular relationships, but it imposes proxyability rules on bean classes and methods because the runtime must be able to create and interpose the proxy.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
