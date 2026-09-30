2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# Completely Fair Scheduler

The Completely Fair Scheduler is Linux's traditional fair scheduling class for ordinary tasks. It models an ideal processor shared among runnable entities and chooses the entity that has received the least weighted service, represented by [[CFS Virtual Runtime]].

Runnable entities are organized in an ordered tree rather than fixed time-slice queues. Nice values influence their weights, and group scheduling can distribute processor time among control groups before dividing a group's share among its tasks.

# References

[[linuxkernelprogramming_secondedition.pdf]]
