2026-10-03 22:25

Status: #baby

Tags: [[Platform FinOps and Cost Management]]

# Autoscaling Cost Tradeoff

The autoscaling cost tradeoff balances sufficient capacity for availability and performance against the expenditure created by additional compute, memory, and storage. Scaling too slowly violates service objectives, while scaling too far, at the wrong signal, or without scaling down can create cost spikes without improving the real business outcome.

Policies need bounded targets, reliable metrics, stabilization, and awareness of provisioning delay. Reactive scaling follows observed demand; predictive scaling can add capacity before a forecast threshold is reached. Both should measure whether the new capacity changed response time or throughput, then remove it when the need has passed.

# References

[[platformengineeringforarchitects.pdf]]
