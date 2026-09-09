2026-09-08 22:09

Status: #baby

Tags: [[Azure Cognitive Vision Applications]]

# Cognitive Service Access Key

A cognitive service access key is the credential a client presents when calling a provisioned Azure cognitive endpoint. The Face API request places the subscription key in its HTTP headers so Azure can associate the call with the correct resource.

The key grants billable service access and should not be treated as harmless application data. The book shows its role directly, but deployment should keep real values out of published source and replace them through protected configuration.

# References

[[c8andnetcore30projectsusingazure.pdf]]
