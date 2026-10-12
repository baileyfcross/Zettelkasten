2026-09-13 20:16

Status: #baby

Tags: [[Large-Scale Software Engineering]]

# Complete Mediation

Complete mediation requires checking every attempted access to every protected object. A permission verified only once may become stale when the user, resource, or policy changes.

Repeated checks prevent cached assumptions from bypassing current authorization rules. Implementations must balance this assurance with performance while keeping the mediation path difficult to evade.

# References

[[computationalthinking.epub]]
