2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebServer Listener Configuration

Helidon listener configuration defines the server socket on which a [[Helidon WebServer]] accepts requests. The WebServer configuration contract includes `ListenerConfig`, and the builder can set properties such as the listening port while also supporting more than one socket.

Setting the port to zero requests an available ephemeral port, which is useful when tests or paired client-server examples must avoid a fixed-port collision. After startup, the application can read the actual bound port from the server and pass it to a client.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
