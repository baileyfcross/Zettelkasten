2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebClient Metrics Service

A Helidon WebClient metrics service instruments selected outbound HTTP methods. The service can define the methods to observe and a naming format, then be attached to the client builder before requests are issued.

In the example, a counter named from the HTTP method and host is registered with the global metric registry. A GET made through the instrumented client increments that counter, connecting outbound-call behavior to the same metrics system used elsewhere in the application.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
