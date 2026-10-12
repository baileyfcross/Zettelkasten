2026-09-17 09:48

Status: #baby

Tags: [[Big Data Law and Individual Rights]] [[Microsoft Foundry Responsible AI Controls]]

# Data Minimization

Data minimization limits collection and retention to information that is adequate, relevant, and no more extensive than the stated purpose requires. It works with [[Purpose Limitation]] by restricting both what enters a system and what remains available for later processing.

Big-data practices strain this principle because future value is often unknown at collection time. The possibility that additional data might reveal a correlation is not by itself a justification for unlimited accumulation.

For Microsoft Foundry agents, minimization also applies to runtime movement of information. A tool should return only the fields needed for the current task, retrieved context should be bounded, and the final response should omit unnecessary sensitive details. Access permission alone does not establish that every accessible field belongs in the prompt, trace, or answer.

# References

[[frontiersofdatascience.pdf]]
[[microsoftfoundryinaction.pdf]]
