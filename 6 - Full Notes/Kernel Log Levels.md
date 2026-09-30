2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Log Levels

Kernel log levels classify a message from emergency conditions through alerts, errors, warnings, notices, information, and debugging. The level is part of the record even when current console policy suppresses its immediate display.

Console verbosity and ring-buffer retention are different concerns: a quiet console can still preserve records for later inspection. Selecting a level according to operational severity lets administrators filter evidence without rewriting the module's logging calls.

# References

[[linuxkernelprogramming_secondedition.pdf]]
