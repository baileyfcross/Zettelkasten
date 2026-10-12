2026-10-11 21:26

Status: #baby

Tags: [[Docker Development and Testing]]

# In-Container Debugger Attachment

In-container debugger attachment connects an IDE on the host to a debug endpoint opened by an application inside a container. The container must start the runtime with debugging enabled, listen on an address reachable through the container network, publish the debug port when necessary, and map container source paths to the host workspace.

Debug endpoints frequently permit deep process control and should not be exposed beyond a trusted development boundary. Debug runtimes, symbols, ports, and relaxed settings should be absent from the production image unless a separately governed diagnostic process requires them.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
