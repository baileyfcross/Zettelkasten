2026-09-06 20:37

Status: #baby

Tags: [[Front-End Service Design]] [[ASP.NET Core Web API Development]]

# Data Transfer Object

A data transfer object is a class shaped specifically for data sent across an application boundary. It can include values required by the client while omitting entity properties that should not be serialized or exposed.

Using a DTO preserves [[Separation of Concerns]] between persistence and presentation. It also gives tests a named, typed result, whereas a quick projection to an anonymous type is less reusable outside the method that created it.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
