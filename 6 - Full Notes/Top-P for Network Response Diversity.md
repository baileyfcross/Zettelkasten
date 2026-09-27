2026-09-27 18:30

Status: #baby

Tags: [[Network AI Model and Prompt Engineering]]

# Top-P for Network Response Diversity

Top-p, or nucleus sampling, restricts token selection to the smallest group whose cumulative probability reaches a chosen threshold. Lowering the threshold narrows the candidate set and generally makes an answer less diverse; raising it permits more alternatives.

For network automation, a narrow response space can support consistency, but it does not prove that the selected command is valid for the target platform. Changing top-p and [[Temperature for Network Response Variability]] at the same time also makes experiments hard to interpret. One control should be varied at a time against a stable prompt and evaluation set.

# References

[[ainetworkingcookbook.pdf]]
