2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Library Path Configuration

R library path configuration determines the directories searched for installed packages and the default destination for new installations. A user library permits installation without changing a system library, while multiple paths can support shared and project-specific collections.

Changing the default permanently requires a startup or environment setting that is applied before package lookup. The configured paths should be inspectable because two libraries may contain different versions of the same package.

# References

[[rprimer.pdf]]
