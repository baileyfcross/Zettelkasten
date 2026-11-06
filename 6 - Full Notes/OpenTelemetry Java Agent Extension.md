2026-11-06 12:32

Status: #baby

Tags: [[Cloud-Native Observability]]

# OpenTelemetry Java Agent Extension

An OpenTelemetry Java agent extension adds automated instrumentation for Java classes, frameworks, or protocols that the standard agent does not recognize. A Java agent intercepts class loading, while ByteBuddy-based extension code identifies target types and methods and injects behavior such as timing, span creation, attribute capture, and context handling without editing the application's source.

A practical sequence begins with manual instrumentation to understand the correct entry points and propagation behavior, then moves the proven pattern into an extension. Profiling can reveal inbound and outbound methods in an unfamiliar component, and extension instrumentation can create spans or inject and extract [[OpenTelemetry Context Propagation|trace context]] around those methods.

The technique is not free. Class transformation, timestamps, logging, extra spans, and header work add runtime overhead, and a faulty extension can create duplicate, missing, or incorrectly related spans. Scope, performance, and propagation therefore need explicit tests before the extension becomes a production replacement for manual code.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
