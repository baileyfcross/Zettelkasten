2026-09-08 22:09

Status: #baby

Tags: [[Azure Cognitive Vision Applications]]

# Azure Face API

The Azure Face API is the cognitive service used by the 2019 mobile project to detect faces and return requested face attributes from an image. The client sends binary image content to the service's detect endpoint with query parameters selecting emotion data.

The response is JSON containing a list of detected faces and their attribute values. The application deserializes it into client-library types, then verifies that exactly one face was returned before choosing a display result.

# References

[[c8andnetcore30projectsusingazure.pdf]]
