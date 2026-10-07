2026-10-07 18:14

Status: #baby

Tags: [[SLES Service Logging and Remote Operations]]

# Chrony Time Synchronization

Chrony synchronizes the system clock with configured time sources while estimating offset, delay, and source quality. Normal correction can slew the clock gradually, while a sufficiently large error may justify a controlled step. NTP strata describe distance from a reference source rather than a simple guarantee of accuracy.

The `chronyc` client exposes source and tracking information needed to verify convergence. Correct time supports logs, authentication, certificates, distributed coordination, and incident reconstruction, so a running daemon is not enough; the administrator should confirm that usable sources are selected and the clock is actually synchronized.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
