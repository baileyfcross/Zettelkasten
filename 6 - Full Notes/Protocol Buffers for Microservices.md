2026-11-06 13:52

Status: #baby

Tags: [[Microservice Communication and Resilience]]

# Protocol Buffers for Microservices

Protocol Buffers encode structured messages from a language-neutral schema and generate readers and writers for participating services. Their compact binary representation reduces bytes transferred and marshaling work across process boundaries compared with more verbose text representations.

Schema evolution depends on field compatibility. A deployed reader can ignore fields added by a newer writer, allowing a message format to grow without requiring every service to be rebuilt at once. This makes the wire schema an explicit contract, but generated code and binary payloads add tooling and reduce the direct human readability available with JSON or XML.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
