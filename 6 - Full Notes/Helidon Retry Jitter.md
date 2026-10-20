2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Retry Jitter

Helidon retry jitter randomly varies the delay between repeated invocations. Given a configured delay and jitter, the effective delay is selected from the interval between delay minus jitter and delay plus jitter, with a negative result clamped to zero.

The jitter unit is configured separately and defaults to milliseconds in the source's annotation table. Jitter changes retry timing without changing which failures qualify under the surrounding [[Helidon Retry Policy]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
