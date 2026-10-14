2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Services and Dedicated Hosting]]

# Game Server Virtual Machine Manager

A game server virtual machine manager is the fleet-level entry point for launching dedicated sessions. It tracks machine capacity, chooses an underutilized virtual machine when one is available, or asks the cloud provider to provision a new machine before instructing its [[Local Server Process Manager]] to launch the game process.

The manager must reconcile asynchronous provisioning, health reports, and simultaneous requests. Without coordination, a traffic spike can cause one new virtual machine per pending match, while aggressive shutdown can remove capacity just before it is needed again. Shared state or regional sharding becomes necessary when several manager instances serve high request volume.

# References

[[multiplayergameprogramming.pdf]]
