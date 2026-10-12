2026-09-27 18:58

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# Amazon SNS Topic

An Amazon Simple Notification Service topic is a publish-subscribe channel. Publishers send a message once to the topic, and SNS delivers copies to subscribed endpoints such as SQS queues, Lambda functions, HTTP endpoints, email addresses, or mobile notification services.

Topics decouple message producers from consumers and support one-to-many delivery. When each consumer needs an independent durable backlog, the topic is commonly combined with queues in the [[SNS Fan-Out]] pattern.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
