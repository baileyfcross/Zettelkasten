2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]] [[Git Version Control]]

# Source Code Repository

A source code repository records versioned application files and provides the revision consumed by the continuous-integration pipeline. A pushed change can serve as the trigger and gives the resulting build an identifiable source state.

The repository is the pipeline's starting contract: build definitions, application code, tests, and relevant deployment scripts must agree at that revision. Generated artifacts are outputs and should not obscure which source produced them.

In Git, a repository includes both the working files and local metadata under `.git`, which stores objects, references, configuration, and history. A repository can be initialized in an existing directory or created by cloning another repository.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[aspnetcore3andreact.pdf]]
