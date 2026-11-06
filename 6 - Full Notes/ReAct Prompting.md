2026-10-31 22:16

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# ReAct Prompting

ReAct prompting interleaves reasoning steps with actions and the observations returned by those actions. The source's cited formulation combines the strengths of [[Chain-of-Thought Prompting|reasoning traces]] and action planning so a model can gather external evidence, revise its next step, and end with a distinct conclusion.

An action must map to an application-controlled tool or retrieval operation rather than executable prose from the model. Tool permissions, input validation, iteration limits, error handling, and observation provenance remain outside the prompt; otherwise an apparently interpretable Thought/Action/Observation sequence can still perform an unsafe action or amplify incorrect evidence.

# References

[[masteringspringai.epub]]
