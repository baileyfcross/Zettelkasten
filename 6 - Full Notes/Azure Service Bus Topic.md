2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]]

# Azure Service Bus Topic

An Azure Service Bus topic accepts a published message and makes independent copies available through one or more subscriptions. Each subscription behaves like a queue with its own retention, delivery, dead-lettering, and consumers, so one event can drive several downstream processes without the publisher addressing each one. Message schema, duplicate handling, sessions, retry safety, and ownership remain part of the application contract.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

