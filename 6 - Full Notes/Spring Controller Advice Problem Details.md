2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring Controller Advice Problem Details

Spring controller advice centralizes exception handling across request-mapped controllers. A `@RestControllerAdvice` class can associate specific exception types with handler methods and return a Problem Details representation containing a safe type, title, status, detail, instance, and selected extension fields.

Centralization gives validation failures and missing resources a consistent [[JSON API Error Response]] without repeating try-catch logic. The handler should catch a specific failure, choose the corresponding HTTP status, and avoid returning stack traces or internal secrets. Custom validation details can help a client repair its request while the standardized outer shape remains stable.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
