2026-09-08 22:09

Status: #baby

Tags: [[Containerized Microservice Architecture]]

# Distributed Transaction Limitation

A distributed transaction limitation appears when one business operation changes state owned by separate services or databases that cannot participate in one ordinary local transaction. At a particular instant, one part may have committed while another has not.

The order-processing discussion contrasts this with a single database transaction that can update an order and stock together. Distributed designs need asynchronous coordination and explicit recovery or compensation rather than assuming every component changes atomically.

# References

[[c8andnetcore30projectsusingazure.pdf]]
