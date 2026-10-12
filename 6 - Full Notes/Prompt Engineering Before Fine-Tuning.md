2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Data and Model Design]]

# Prompt Engineering Before Fine-Tuning

Prompt engineering should normally precede fine-tuning when adapting a foundation model. Clear instructions, output constraints, edge-case rules, and a few representative input-output examples can control tone, format, and task behavior without training a new model variant.

Fine-tuning becomes justified when prompting cannot produce consistent domain behavior and a sufficient set of high-quality labeled examples exists. It adds dataset preparation, training compute, testing, ownership questions, and recurring maintenance when requirements change. Trying the lower-cost prompt path first clarifies whether the remaining problem is actually a learned pattern rather than an underspecified instruction.

# References

[[microsoftfoundryinaction.pdf]]
