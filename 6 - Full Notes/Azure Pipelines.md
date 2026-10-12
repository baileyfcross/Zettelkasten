2026-09-27 11:41

Status: #baby

Tags: [[Azure DevOps Work Planning and Traceability]]

# Azure Pipelines

Azure Pipelines automates build, test, packaging, and deployment steps from a version-controlled source. Pipeline results connect a particular code revision to the evidence and artifacts produced by the delivery process.

Within project planning, that evidence helps distinguish work that was merely changed from work that was integrated and releasable. Pipeline automation requires explicit triggers, environments, credentials, and failure handling.

In an Azure DevSecOps design, the pipeline is also an enforcement and evidence path. Pull-request checks, dependency and secret scanning, static analysis, infrastructure validation, image scanning, signed artifacts, and environment approvals can prevent known weaknesses from advancing. These controls need risk-based thresholds and constrained workload identities so that automation raises security quality without granting the delivery system unlimited production privilege.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
