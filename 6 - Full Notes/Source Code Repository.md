2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Source Code Repository

A source code repository records versioned application files and provides the revision consumed by the continuous-integration pipeline. A pushed change can serve as the trigger and gives the resulting build an identifiable source state.

The repository is the pipeline's starting contract: build definitions, application code, tests, and relevant deployment scripts must agree at that revision. Generated artifacts are outputs and should not obscure which source produced them.

# References

[[aspnetcore3andreact.pdf]]
