2026-09-27 12:11

Status: #baby

Tags: [[AI Agent Observability and Evaluation]]

# OpenTelemetry Instrumentation for Agents

OpenTelemetry instrumentation gives agent workflows a common path for exporting logs, traces, and metrics. Custom activities can cover input loading, specialist execution, coordination, and evaluation, while model-client instrumentation records calls made inside those workflow spans.

A shared service identity, activity source, meter, and OTLP exporter let local and production backends consume the same signals. Counters and histograms can record workflow runs, failures, agent responses, evaluation scores, and duration, making orchestration behavior visible through standard observability tools.

The useful span boundary begins at request receipt and continues through retrieval, the model call, policy evaluation, tool invocation, verification, and audit persistence. Instrumenting only the LLM call measures a dependency but cannot show which action was authorized, whether its post-condition passed, or where an agent incident crossed into the operating system.

# References

[[agenticaifordevopsengineers.pdf]]

[[ultimateaiguideforlinuxengineers.pdf]]
