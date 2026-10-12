2026-09-27 21:45

Status: #baby

Tags: [[Azure Network and Resilience Architecture]]

# Azure Route Server

Azure Route Server exchanges Border Gateway Protocol routes between virtual networks and network virtual appliances. Dynamic advertisement lets appliances learn Azure prefixes and lets Azure learn appliance routes without manually maintaining every user-defined route. Route selection still follows Azure precedence: sufficiently specific learned routes can override system routes, while user-defined routes take priority, so architects must understand how multiple sources combine.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

