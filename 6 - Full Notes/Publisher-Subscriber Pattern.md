2026-09-21 22:12

Status: #baby

Tags: [[Cloud Messaging Caching and Operations Patterns]]

# Publisher-Subscriber Pattern

The publisher-subscriber pattern sends an event from a producer to whichever consumers have registered interest in that event. A customer service can publish a customer-created event while an order service updates its own store and a separate service sends a welcome message. The producer does not need direct knowledge of either consumer, making it easier to add or replace reactions, but subscribers must agree on the event's meaning and delivery behavior.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

