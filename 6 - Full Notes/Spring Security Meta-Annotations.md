2026-11-08 16:45

Status: #baby

Tags: [[Spring Security and Identity]]

# Spring Security Meta-Annotations

A Spring Security meta-annotation packages a repeated authorization or principal-resolution rule behind a purpose-specific annotation. A method can state that an operation requires a CRM administrator, for example, without embedding the same expression string in every controller and service.

Centralization makes the policy easier to change and gives code reviewers a recognizable vocabulary. The annotation must still expand to a supported security expression or argument resolver, and its name should describe the actual permission rather than a vague implementation detail. It complements rather than replaces [[Spring Security Request Authorization Rules]].

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
