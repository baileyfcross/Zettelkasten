2026-09-21 22:12

Status: #baby

Tags: [[Cloud Scalability and Resilience Patterns]]

# Auto-Scaling

Auto-scaling changes capacity automatically in response to a schedule or measured condition. The book's App Service example adds instances when average CPU use crosses an upper threshold and removes them below a lower threshold, within minimum and maximum limits. Hysteresis and bounds prevent constant oscillation, while the chosen signal must reflect the real bottleneck; adding web instances will not fix a saturated shared database.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

