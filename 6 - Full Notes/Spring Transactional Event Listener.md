2026-11-08 16:45

Status: #baby

Tags: [[Spring Messaging and Integration]]

# Spring Transactional Event Listener

A Spring transactional event listener binds event handling to a phase of the current transaction. An after-commit listener acts only when the database work succeeds, preventing side effects such as a welcome message from being triggered for a record that was rolled back.

The listener still runs within the application's event mechanism and does not by itself make an external side effect atomic with the database commit. Failures after commit need retry, durable messaging, or an outbox-style design when loss is unacceptable. The phase expresses when the reaction is eligible, while the handler's delivery guarantees remain a separate concern.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
