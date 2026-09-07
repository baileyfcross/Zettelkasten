2026-09-06 22:42

Status: #baby

Tags: [[Real-Time IoT Stream Processing]]

# Elastic Stream Scaling

Elastic stream scaling changes the resources assigned to streaming operators as event rates rise or fall. Partitioned operators can add workers during a burst and release them when demand subsides.

Moving state and repartitioning keys take time and can disrupt ordering, so a controller should react early enough to prevent queues without oscillating after every short fluctuation.

# References

[[bigdatamanagementandprocessing.pdf]]
