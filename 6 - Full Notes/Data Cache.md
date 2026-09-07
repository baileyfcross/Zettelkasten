2026-09-06 20:52

Status: #baby

Tags: [[Web Performance and Scalability]]

# Data Cache

A data cache keeps a reusable result closer to the application so repeated requests do not always query the database. In-memory caching can shorten a read path for data whose temporary reuse is acceptable.

Caching introduces a freshness decision. The application needs a key, an expiration policy, and a reasoned response to writes so that lower latency does not silently serve unsuitable old data.

# References

[[aspnetcore3andreact.pdf]]
