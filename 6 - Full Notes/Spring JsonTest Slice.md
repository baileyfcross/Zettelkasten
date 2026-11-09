2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# Spring JsonTest Slice

`@JsonTest` loads JSON mapping infrastructure without the web server or business application. It configures a Jackson tester so a record or DTO can be serialized and deserialized against an expected document independently of controller behavior.

The slice is valuable for custom property names, ignored values, date formats, record constructors, and compatibility-sensitive payloads. A mapping test catches a contract change close to its source, while a web test remains responsible for the chosen media type and HTTP response. It should assert meaningful fields rather than an incidental textual ordering when order is not part of the contract.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
