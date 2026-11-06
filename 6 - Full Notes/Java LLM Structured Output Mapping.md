2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Java LLM Structured Output Mapping

Java LLM structured output mapping converts a generated response into a declared Java type such as a record, POJO, list, or enum. The frameworks described in the source derive or supply format instructions and then parse the response for use by ordinary application code.

Typed mapping improves integration compared with manually splitting prose, but a successfully parsed object is not necessarily truthful or complete. Validation rules, null handling, retries, and domain checks must follow deserialization before the object drives a consequential action.

The Spring AI 0.8.1 example in the current source uses a `BeanOutputParser` to derive format instructions from a Java class, inserts those instructions into a [[Spring AI Prompt Template|prompt template]], and parses the returned JSON into the declared object. The format placeholder and parser form one contract: changing the target fields or prompt without testing both can produce well-formed but semantically incomplete objects.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
