2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# Spring WebFluxTest Slice

`@WebFluxTest` loads reactive web infrastructure and selected controllers or functional handlers while excluding unrelated application components. It configures a WebTestClient that can drive the reactive route without opening a real network connection.

The slice verifies route selection, request decoding, reactive response production, validation, and error mapping. Dependencies outside the web layer should be replaced deliberately, and the test must not call blocking operations inside the reactive path. Database behavior belongs in a data slice such as the R2DBC test support or in a container-backed integration test.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
