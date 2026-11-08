2026-11-08 14:08

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# Jakarta REST Exception Mapper

A Jakarta REST exception mapper converts a selected Throwable type into an HTTP Response through the ExceptionMapper toResponse method. Marking the mapper as a Provider lets the runtime discover and register it as a REST component.

The mapper separates exception detection from the client-facing contract. For example, a constraint-violation mapper can collect the affected fields and validation messages and return them with a 400 response instead of exposing only a generic bad-request result. Centralized mapping makes status codes and error representations consistent across resource methods that can raise the same failure.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
