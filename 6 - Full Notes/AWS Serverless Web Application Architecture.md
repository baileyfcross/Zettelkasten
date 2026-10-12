2026-09-27 20:01

Status: #baby

Tags: [[AWS Application Integration and Analytics]]

# AWS Serverless Web Application Architecture

An AWS serverless web application can deliver static frontend assets through Amazon S3 and CloudFront, authenticate users with Cognito, expose APIs through [[Amazon API Gateway]], execute business logic in Lambda, and persist data in DynamoDB. Each managed component scales independently and reduces server administration. The architecture remains a distributed system: authorization, retries, quotas, observability, deployment compatibility, and data consistency must be designed across service boundaries.

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

