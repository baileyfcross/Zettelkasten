2026-10-07 18:14

Status: #baby

Tags: [[SLES Service Logging and Remote Operations]]

# tmux Persistent Terminal Sessions

Tmux is a terminal multiplexer that keeps a server-side session containing windows and panes independently of one attached client. An SSH connection can detach or fail while the session and its running terminal programs remain available for later reattachment.

This makes tmux useful for long administrative observations or interactive work that must survive an unreliable network. Persistence is not job supervision: critical services should still run under systemd or another appropriate manager, and output needed for audit or recovery should not exist only in a scrollback buffer.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
