2026-09-27 11:07

Status: #baby

Tags: [[ASP.NET Core API Integration Testing]]

# Request Validation Test

A request validation test submits an invalid API payload and checks the public failure response. It verifies that binding and validation reject the request before application behavior proceeds, and that the returned status and error document are useful to a client.

The test should cover meaningful rules such as missing required data, invalid ranges, or inconsistent fields. Assertions belong on the stable error contract rather than incidental internal exception text.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
