2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure Deployment Slot

An Azure deployment slot is a separately addressable App Service environment associated with an application. A release can be deployed to a staging slot and exercised there before the slot is swapped into the production position.

Slots reduce the need to replace production files in place. Settings must be classified carefully so environment-specific values remain with the intended slot during a swap.

# References

[[aspnetcore3andreact.pdf]]
