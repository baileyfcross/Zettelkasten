2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Spring Boot AI Auto-Configuration

Spring Boot AI auto-configuration creates model-related beans from a selected Spring AI starter and application properties. In the source's examples, provider credentials, endpoints, and model names are externalized while controllers and services receive configured clients through dependency injection.

Auto-configuration shortens setup but can obscure which provider, options, or advisors are active. Production applications should keep configuration profiles reviewable, protect credentials outside source control, and verify the assembled context when deployments differ.

The current source inspects the Spring AI 0.8.1 auto-configuration JAR to show that provider URLs, default model names, and connection properties may be supplied before application code runs. It then overrides selected values in `application.yaml`, including a Bedrock region, credentials supplied through environment variables, model enablement, and temperature. Reviewing the effective configuration is therefore part of verifying which model call the injected client will make.

The book extends the idea into a reusable CRM assistant starter. Auto-configuration registers the assistant only when ChatClient is present, enables typed properties, lets a property disable the feature, and backs away when the consuming application provides its own assistant bean. Separating that logic from the lightweight dependency-aggregating starter preserves both a one-dependency experience and user override control.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
