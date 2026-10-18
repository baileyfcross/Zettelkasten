2026-10-18 15:54

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Consumer-Driven Contract Testing

Consumer-driven contract testing records the requests and responses that a consumer actually relies on, then verifies that the provider satisfies that agreement. A consumer can generate a contract while testing its client behavior, and the provider can verify the same contract in its delivery pipeline without deploying the whole system.

This provides early evidence that independently released services remain compatible. It does not replace provider logic tests or a small number of end-to-end flows, and the contracts themselves must be maintained as consumers evolve. A provider may add compatible fields, but changing or removing behavior used by a verified consumer should fail before release. The technique protects [[Independent Microservice Deployment]] by making interface dependencies executable.

# References

[[artofdecodingmicroservices.epub]]
