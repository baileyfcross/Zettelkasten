2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Event Observer

Jakarta CDI events let one component fire a typed payload without a compile-time dependency on the beans that receive it. The container matches observer methods to events by payload type and qualifiers. A synchronous observer uses Observes and runs on the firing thread, while an asynchronous event fired through fireAsync is delivered to compatible asynchronous observers and returns a CompletionStage.

Transactional observers can defer synchronous notification to phases such as before completion, after completion, after failure, or after successful commit. Event metadata gives observers access to the event type, qualifiers, and injection-point information, and conditional observation can require the observer's containing bean to already exist in its active scope.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
