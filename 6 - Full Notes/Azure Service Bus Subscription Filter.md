2026-09-27 21:45

Status: #baby

Tags: [[Azure Cloud-Native Application Architecture]]

# Azure Service Bus Subscription Filter

An Azure Service Bus subscription filter selects which topic messages are copied into a subscription according to system or application properties. Filters let consumers receive categories such as valid, auto-approved, or approval-required invoices without separate publishers. The publisher must promote reliable metadata for the rule to inspect; filtering on properties that an output binding does not preserve can silently break routing and requires lower-level message control.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

