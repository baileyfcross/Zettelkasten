2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Spring AI Advisors Chain

A Spring AI advisor chain intercepts a ChatClient request and response so reusable behavior can be applied around a model call. The source uses advisors as a place for concerns such as conversational memory, retrieval augmentation, logging, or other prompt and response transformations.

Advisor order matters because one advisor may depend on the context produced by another. A chain should therefore be treated as an explicit workflow with observable inputs and outputs, not as invisible decoration whose effects are assumed to commute.

The current source's production example places a `QuestionAnswerAdvisor` around a chat request so it can search the configured vector store and attach retrieved documents before generation. Those documents are also available in response metadata for evaluation, connecting the advisor's runtime augmentation to [[Spring AI Relevancy Evaluator|relevancy testing]] rather than treating retrieval as an invisible side effect.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
