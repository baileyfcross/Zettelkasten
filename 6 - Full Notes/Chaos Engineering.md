2026-09-05 15:58

Status: #baby

Tags: [[Live Game Operations]]

# Chaos Engineering

Chaos engineering deliberately introduces controlled failures to test whether a live system and its operators behave as expected under stress. Experiments begin with explicit hypotheses and bounded impact, then observe detection, degradation, and recovery.

The purpose is to reveal hidden assumptions before uncontrolled failure does. It requires safeguards, monitoring, and progressively increased scope rather than indiscriminate disruption.

The observability source uses controlled experiments for a second purpose: producing labeled failure evidence. Network loss, latency, policy drops, and other bounded faults can verify that traces, metrics, system signals, dashboards, and alerts expose the expected mechanism. A well-recorded experiment can then become a reproducible case in an [[Operations Knowledge Base]] rather than disappearing after the resilience test.

# References

[[agilegamedevelopment2e.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
