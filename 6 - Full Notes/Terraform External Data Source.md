2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform External Data Source

The external data source runs a local program and exchanges a JSON object through standard input and output. It lets Terraform read information that no ordinary provider exposes, after which the returned values can feed resources or a [[Terraform Output Value]].

The program must be available wherever Terraform runs, return valid JSON, and exit successfully, so it adds an environmental dependency that normal provider installation does not manage. It should remain a narrow adapter for reading data, not a concealed provisioning engine. Side effects performed by the program are invisible to [[Terraform State]] and cannot be planned, updated, or destroyed reliably.

# References

[[masteringterraform.pdf]]

