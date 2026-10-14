2026-10-04 15:18

Status: #baby

Tags: [[Information Systems Research Methods]]

# Discrete-Event Simulation

Discrete-event simulation represents a system whose state changes at distinct event times. Entities occupy states or sets, events cause instantaneous changes, activities consume modeled time, and delays occur when an entity waits for a condition or resource.

An event-scheduling implementation keeps a future-event list ordered by simulated time. It advances the clock to the next event, updates the system state, records relevant measures, schedules resulting events, and continues until a stopping event or rule is reached. This avoids calculating every uneventful instant between changes.

Credible use requires validated input data, verification of the implementation, validation of the model, an explicit experimental design, enough independent runs, and documentation of assumptions. Initial transient behavior can bias steady-state measures, so warm-up handling and run length belong in the design rather than being chosen after the output is seen.

# References

[[researchmethodsforinformationsystems.pdf]]
