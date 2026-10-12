2026-09-27 11:48

Status: #baby

Tags: [[Continuous Delivery Risk and Release Governance]] [[Production Network Agent Operations]]

# Feature Flag

A feature flag separates deployment of code from exposure of a feature. The new path can remain disabled, enabled for selected users or environments, and activated when its behavior is ready to deliver value.

Flags reduce the need for long-lived branches but add runtime states that must be tested and eventually removed. A flag is a temporary control, not a permanent substitute for coherent configuration or design.

For a production network agent, flags can enable approved read-only tools while keeping broad show-command or write capabilities disabled. The tool policy should be adjustable without changing the prompt or redeploying the model, which lets a pilot expand by device, user group, or capability. A feature flag narrows scope; a separate [[Network Agent Kill Switch]] provides the emergency stop for the workflow as a whole.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
