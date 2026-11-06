2026-11-06 12:32

Status: #baby

Tags: [[Cloud-Native Observability]]

# Legacy Middleware Trace Bridge

A legacy middleware trace bridge preserves diagnostic continuity through a component that cannot emit a standard distributed span. It can combine an integration server, structured logs, business identifiers, profiles, events, custom SDK instrumentation, or bytecode probes to represent the component's inbound work, internal latency, and outbound work.

The source recommends first profiling a black box to find the methods and threads that receive and send requests. A Java component may then use an [[OpenTelemetry Java Agent Extension]] to create spans and handle headers without changing source code. When direct instrumentation is impossible, logs can record trace and business context and events can connect the traces created on either side.

The bridge should preserve what is observed rather than fabricate a continuous parent-child tree. A [[Business-to-System Correlation Chain]] can place several traces under the same transaction, while explicit gaps remain visible for later validation and improvement.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
