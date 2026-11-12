2026-11-11 18:27

Status: #baby

Tags: [[Software Design Principles]]

# Information Hiding

Information hiding decomposes a system around design decisions that other modules should not need to know. A module owns a representation or rule and exposes operations through a stable interface, so callers depend on what it provides rather than how it stores or performs the work.

This differs from dividing a program only by execution order. When a representation changes, a change-oriented module contains the impact; a control-flow decomposition may spread knowledge of the same representation across several steps.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

