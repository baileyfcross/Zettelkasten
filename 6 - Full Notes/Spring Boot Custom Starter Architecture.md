2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# Spring Boot Custom Starter Architecture

A professional Spring Boot custom starter commonly separates an auto-configuration module from a lightweight starter module. The auto-configuration module contains properties, conditional bean definitions, and implementation setup; the starter aggregates that module and the dependencies an adopter needs for a one-dependency integration experience.

The separation keeps configuration logic distinct from dependency packaging and lets provider-specific choices remain optional. Boot discovers the auto-configuration through the imports metadata under `META-INF/spring`, while [[Spring Boot Conditional Starter Beans]] determines whether its beans should exist. An explicit [[Spring Boot Enable Annotation Pattern]] can supplement automatic discovery when the feature should require opt-in.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
