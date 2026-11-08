2026-10-19 22:48

Status: #baby

Tags: [[MicroProfile and Jakarta Standards]]

# MicroProfile Core and Standalone Specifications

MicroProfile distinguishes a core platform set from stand-alone specifications that an implementation or application can adopt separately. The boundary changes as the ecosystem converges on other standards or vendors make different implementation choices.

The book records Open Tracing moving out of the core set after OpenTracing and OpenCensus converged into OpenTelemetry and MicroProfile Telemetry emerged. Metrics similarly became stand-alone in MicroProfile 7.0 because some vendors chose Micrometer instead, showing that platform membership is version-specific rather than permanent.

The second source likewise presents MicroProfile as a mix of common platform capabilities and independently usable specifications. Applications should therefore state the particular specification and version they depend on instead of assuming that every MicroProfile runtime bundles every historical API under one immutable platform definition.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
