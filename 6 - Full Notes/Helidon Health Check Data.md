2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Health Check Data

Helidon health-check data consists of optional key-value details attached to an individual response. A check can record the resource and check type along with measurements such as heap usage, maximum memory, or CPU load.

The data explains why a procedure reported its current status without changing the aggregate `UP` or `DOWN` calculation. Because the fields appear in the GET response, they should be diagnostic values appropriate for clients of the health endpoint.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
