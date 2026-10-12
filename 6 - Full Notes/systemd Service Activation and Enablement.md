2026-10-07 18:14

Status: #baby

Tags: [[SLES Service Logging and Remote Operations]]

# systemd Service Activation and Enablement

Starting a systemd service requests activation now, while enabling it installs the relationships that make it start when a future target or trigger is reached. A service may therefore be running but disabled, or enabled but presently stopped. Stopping and disabling express the corresponding runtime and future-activation changes.

Keeping these states separate prevents a successful manual test from being mistaken for persistent configuration. Status, unit dependencies, logs, and the enablement state should all be checked when a daemon behaves differently after reboot. Socket, path, timer, or dependency activation may also start a service that was not enabled directly.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
