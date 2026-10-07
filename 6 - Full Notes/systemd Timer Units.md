2026-10-07 18:14

Status: #baby

Tags: [[SLES Service Logging and Remote Operations]]

# systemd Timer Units

A systemd timer schedules activation of another unit at a calendar time, after a relative interval, or according to boot and activation events. The timer defines when work should occur, while the associated service defines what work runs and under which identity, environment, and dependency rules.

SLES 16 recommends timers for scheduled service work because they integrate with the same status, dependency, enablement, and journal mechanisms as other units. Reliable scheduling still requires checking both units: an active timer can trigger a service that then fails, and a correct service will never run if its timer is disabled or incorrectly specified.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
