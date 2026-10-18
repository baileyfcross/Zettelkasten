2026-09-30 17:53

Status: #baby

Tags: [[LLM-Assisted Software Testing]] [[Prompt-Controlled Generative AI Applications]]

# Hallucination Control in AI Testing

Hallucination control in AI testing grounds model output in code, requirements, static findings, runtime results, and retrieved documentation. Structured prompts and tools reduce unsupported claims, while independent execution determines whether a proposed test or repair actually works.

The model should be allowed to report insufficient context instead of inventing APIs or behavior. Explanations, citations, confidence signals, and human review make uncertainty visible but do not substitute for compile, test, and security checks.

The Java bot source supplies a concrete acceptance test: a support bot grounded in a mobile-app FAQ claims that an unsupported desktop-only authentication feature is available and invents another feature absent from the file. Comparing the response against the supplied facts exposes the failure. Revising the system instruction to use only the FAQ and decline unsupported assumptions is a control that must be retested with questions both inside and outside the knowledge boundary.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
[[chatgptforjava.epub]]
