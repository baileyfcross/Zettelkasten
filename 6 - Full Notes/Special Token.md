2026-09-30 17:53

Status: #baby

Tags: [[Large Language Model Foundations]]

# Special Token

A special token is a reserved vocabulary item that represents structure or control rather than an ordinary word fragment. Beginning, ending, padding, separation, or unknown-token markers let training and generation identify boundaries and batch sequences consistently.

The tokenizer must map each special token to a stable index, and the model configuration must agree with those mappings. Adding boundary tokens can prevent a generator from blending one training sample into the next and provide an explicit stopping condition.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
