2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Services and Dedicated Hosting]]

# Game Server Capacity Scaling

Game server capacity scaling adjusts the number of active machines and processes to match session demand. Scale-out provisions capacity when no existing host can accept a game; scale-in retires empty capacity after a policy determines that it is unlikely to be needed soon.

Immediate reactions can amplify short spikes: several concurrent requests may each provision a machine, and shutting down the moment a host becomes empty can cause repeated churn. Pending capacity, cooldown periods, regional demand, and configurable utilization thresholds make the policy more stable. High launch rates can require multiple managers and a shared fast state store.

# References

[[multiplayergameprogramming.pdf]]
