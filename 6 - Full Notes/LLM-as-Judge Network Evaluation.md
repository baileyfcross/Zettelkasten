2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# LLM-as-Judge Network Evaluation

LLM-as-judge network evaluation asks a separate model to score saved answers against stated criteria such as accuracy, completeness, clarity, and relevance. It can apply a common rubric quickly across many candidate responses and produce explanations alongside numerical scores.

The judge is another probabilistic system and may favor its own style or miss a subtle configuration error. Its scores should be calibrated against expert-reviewed examples and never replace syntax checks or lab tests. Keeping raw answers and explanations visible allows engineers to challenge the ranking before [[Cost-Adjusted Network Model Selection]].

# References

[[ainetworkingcookbook.pdf]]
