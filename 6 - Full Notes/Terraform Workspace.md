2026-09-30 23:18

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Workspace

A Terraform workspace gives one root configuration a distinct [[Terraform State]], allowing the same code to represent instances such as development, test, and production. Switching workspaces changes the state context, not the configuration or the structure of the deployment.

Workspaces are convenient when environments share code and operating boundaries. They are weaker isolation when instances need different permissions, release ownership, failure domains, or control planes. Large workspaces also make every [[Terraform Plan]] inspect more resources, so a [[Terraform Layered Workspace Architecture]] may offer safer blast radii than placing an entire platform in one state.

# References

[[masteringterraform.pdf]]

