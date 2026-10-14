2026-09-30 23:18

Status: #baby

Tags: [[Terraform Core Workflow and State]]

# Terraform Apply

`terraform apply` executes the actions selected by a [[Terraform Plan]], using the [[Terraform Dependency Graph]] to order dependent work and parallelize independent work. Successful operations update [[Terraform State]] so later plans know which configuration addresses correspond to real objects.

Applying a saved [[Terraform Plan Artifact]] preserves the action set that reviewers approved. Applying without one recalculates a plan immediately before execution, which can be useful interactively but weakens separation between review and change. A targeted apply is an exceptional tool for bootstrapping or recovery; routine use can leave the wider configuration only partially reconciled.

# References

[[masteringterraform.pdf]]

