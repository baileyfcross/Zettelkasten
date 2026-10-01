2026-09-30 23:37

Status: #baby

Tags: [[Windows Remote Desktop Services]]

# Remote Desktop Drain Mode

Remote Desktop drain mode stops a Session Host from accepting ordinary new sessions while allowing existing users to continue working. Depending on the selected behavior, reconnection to an existing session may still be permitted. The host gradually empties as users sign out, creating a controlled maintenance window without abruptly terminating the whole user population.

Draining is a placement control, not proof that the server is idle. Administrators should monitor remaining sessions, communicate deadlines, and handle disconnected sessions before patching or rebooting. After maintenance, the host must be returned to normal connection acceptance and verified through the broker. A multi-host collection makes this practice useful because new sessions can land elsewhere; a single-host collection cannot provide continuity simply by refusing its only endpoint.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
