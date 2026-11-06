2026-10-31 22:16

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Spring AI Prompt Template

A Spring AI prompt template stores reusable model instructions with named placeholders that application code fills at runtime. In the source's Spring AI 0.8.1 examples, `PromptTemplate` loads a StringTemplate resource, binds values such as a theme or intensity, and creates a `Prompt` containing the messages sent through the chat client.

Keeping the template outside controller logic separates stable instructions from request data and makes the prompt easier to reuse and revise. Placeholders still require controlled inputs, and a template that requests structured data should change together with its [[Java LLM Structured Output Mapping|output parser]], tests, and [[Versioned Prompt Contracts|versioned contract]].

# References

[[masteringspringai.epub]]
