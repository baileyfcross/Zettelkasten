2026-09-08 22:09

Status: #baby

Tags: [[Azure Blob and Queue Storage]]

# Azure Storage Account

An Azure Storage account is the managed resource that contains Azure blob, file, table, and queue services under shared configuration and credentials. The book creates accounts for photo blobs and for queued sales-order messages.

The account's performance tier, access model, replication, location, and connection information affect cost and behavior. Application code obtains a service-specific client from the account rather than treating every storage form as the same API.

The Azure architecture map further treats the storage account as a security, network, and resilience boundary. Private endpoints, firewall rules, managed identity, shared-key restrictions, encryption keys, redundancy, diagnostic settings, and lifecycle policy are selected at account or service scope. Grouping unrelated workloads into one account can couple their blast radius, throughput limits, governance, and recovery choices even when they use different storage services.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
