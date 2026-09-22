2026-09-21 22:12

Status: #baby

Tags: [[Software Design Principles]]

# Open-Closed Principle

The open-closed principle favors extending behavior through a defined contract while keeping established client-facing behavior stable. A caller that depends on an interface can accept a new implementation without rewriting the caller for each variant. The useful boundary is the one likely to vary; adding an interface for every class before variation appears can make the design more complex without improving extensibility.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

