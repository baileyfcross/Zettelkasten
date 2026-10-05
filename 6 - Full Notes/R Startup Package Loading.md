2026-10-04 22:20

Status: #baby

Tags: [[R Package Workspace and System Operations]]

# R Startup Package Loading

R startup package loading places attachment commands in a startup profile so selected packages become available automatically when a session begins. This can make a personal interactive environment convenient, but it also makes scripts depend on state not visible in the script itself.

Reusable analyses should still attach or namespace their dependencies explicitly. Startup customization should be small, documented, and tested because errors in the profile affect every new session.

# References

[[rprimer.pdf]]
