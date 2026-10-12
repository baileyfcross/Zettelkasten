2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# RemoteApp

RemoteApp publishes an application running on a Remote Desktop Session Host so it appears to the user as an individual window rather than as a complete remote desktop. The program still executes inside an RDS session and consumes the host's resources, but local presentation reduces the visual boundary between remote and local applications.

Programs are published through a collection and can be assigned to approved user groups, then discovered through Web Access, a workspace feed, or connection files. File associations, clipboard and device redirection, printing, and authentication influence how integrated the application feels. RemoteApp narrows the presented interface but is not an application sandbox; users and the program still operate within a shared Session Host that needs multi-user hardening and capacity planning.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
