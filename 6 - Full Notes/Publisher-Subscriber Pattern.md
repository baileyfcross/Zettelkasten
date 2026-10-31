2026-09-21 22:12

Status: #baby

Tags: [[Cloud Messaging Caching and Operations Patterns]] [[.NET Microservice Communication and Workers]]

# Publisher-Subscriber Pattern

The publisher-subscriber pattern sends an event from a producer to whichever consumers have registered interest in that event. A customer service can publish a customer-created event while an order service updates its own store and a separate service sends a welcome message. The producer does not need direct knowledge of either consumer, making it easier to add or replace reactions, but subscribers must agree on the event's meaning and delivery behavior.

The book uses publish-subscribe to let an event source notify interested handlers without depending directly on each receiver. That reduces structural coupling while making event contract, ordering, and duplicate delivery part of the design.

In the Java microservice source, a topic supplies one copy of a published event to each subscribed output channel. A new service can subscribe as the application evolves without changing or restarting the publisher, while each subscriber still consumes its own copy only once according to that channel's delivery behavior.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
