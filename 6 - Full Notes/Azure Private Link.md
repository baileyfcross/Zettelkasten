2026-09-27 21:45

Status: #baby

Tags: [[Azure Network and Resilience Architecture]]

# Azure Private Link

Azure Private Link gives a supported managed service a private endpoint with an IP address inside a customer virtual network. Workloads reach that endpoint without exposing the service through its public interface, while the provider publishes a private-link alias behind the scenes. The network path and DNS name must agree: private DNS commonly maps the service’s normal hostname to the private endpoint address inside the trusted network.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

