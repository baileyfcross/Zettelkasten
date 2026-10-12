2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]] [[.NET Core Data Types and Collections]]

# Garbage Collection

Garbage collection reclaims managed objects that are no longer reachable. Frequent temporary allocations increase the amount of memory the collector must examine and can add work to a heavily used request path.

The book compares custom request parsing with ASP.NET Core model binding to reduce unnecessary object creation. Allocation changes should be measured under load because simpler code and lower allocation may matter more than hand-written parsing assumptions.

The managed heap is organized into generations so short-lived objects can usually be collected without scanning every older object. Collection traces reachable objects, reclaims unreachable space, and may compact surviving objects; a finalizable object follows an additional path before its memory can be reclaimed.

# References

[[aspnetcore3andreact.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
