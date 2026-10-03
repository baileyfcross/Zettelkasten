2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Services and Dedicated Hosting]]

# Game Server Provisioning

Game server provisioning obtains compute capacity and starts the process that will host a requested match. A fleet manager first searches for an existing machine with room; if none exists, it requests a virtual machine from the cloud provider, waits for initialization, contacts the local process manager, and launches the server instance.

Provisioning is asynchronous and slower than selecting warm capacity, so matchmaking must represent a pending state and handle failure. Images, startup configuration, ports, and process limits must be consistent enough that a newly created machine can join the fleet without manual repair.

# References

[[multiplayergameprogramming.pdf]]
