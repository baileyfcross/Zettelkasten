2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Build Agent

A build agent is the execution environment that runs the steps in a build pipeline. It checks out the source, invokes the required toolchains, executes tests, and places generated files where the pipeline can publish them.

The agent's installed tools and operating environment affect whether a build is reproducible. Pipeline steps should declare the needed runtime behavior rather than depend on accidental machine state.

# References

[[aspnetcore3andreact.pdf]]
