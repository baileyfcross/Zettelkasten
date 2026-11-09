2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring Application Event Publisher

Spring `ApplicationEventPublisher` broadcasts an event object to interested listeners inside one application context. The event can be an ordinary record, and `@EventListener` selects it from the listener method's parameter type, allowing additional reactions to be introduced without changing the publisher.

Publication is synchronous by default, so a slow listener delays the calling operation. An asynchronous listener requires enabled async execution and a suitable executor, while [[Spring Transactional Event Listener]] is preferable when a reaction must occur only after a surrounding database transaction commits. Application events decouple beans, not independently deployed services.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
