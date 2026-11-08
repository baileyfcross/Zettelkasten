2026-11-06 13:52

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# CAP Theorem

The CAP theorem describes a constraint among consistency, availability, and partition tolerance in a distributed system: all three cannot be guaranteed simultaneously when a partition must be handled. In the book's microservice framing, consistency gives nodes the same view of data, availability keeps operations responsive, and partition tolerance lets the application continue despite failed communication between nodes.

The theorem turns service distribution into a business choice rather than a purely technical one. An order and inventory system can remain available during separation while temporarily presenting an order that later must be canceled, or it can reject work until a consistent answer is available. [[BASE Transaction]] and [[Eventual Consistency]] make the first choice explicit; operations that cannot tolerate an interim answer need a stronger [[Atomic Consistency Boundary]].

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
