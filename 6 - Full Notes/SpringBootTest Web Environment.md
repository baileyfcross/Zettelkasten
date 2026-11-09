2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# SpringBootTest Web Environment

`@SpringBootTest` loads the full Boot application context for a test that crosses several application layers. Its mock web environment supplies a servlet context without a live port, a random-port environment starts the embedded server on an available socket, and a non-web environment loads the context without starting a server.

The choice should match what the test claims to verify. A random port exercises real HTTP serialization and server configuration with [[Spring RestTestClient]], while a focused controller test can avoid full startup. Test properties can override configuration for the class, but broad context loading is slower and less isolating than a suitable slice.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
