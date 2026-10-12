2026-09-27 21:45

Status: #baby

Tags: [[Azure Security Architecture and Operations]]

# Azure Hold Your Own Key

Hold Your Own Key keeps cryptographic key material under customer custody, often in customer-controlled hardware, rather than making it continuously available to a managed cloud service. This offers stronger sovereignty and separation but narrows service compatibility and increases operational complexity. Because many platform services must access a key to serve data, HYOK is most practical for selected infrastructure or specialized workloads whose custody requirements justify reduced managed-service convenience.

# References

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
