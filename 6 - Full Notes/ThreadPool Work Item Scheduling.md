2026-09-27 00:11

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]]

# ThreadPool Work Item Scheduling

The .NET thread pool maintains reusable worker threads and assigns queued work to them, avoiding the repeated cost of creating and destroying a dedicated thread for every short operation. Tasks commonly use this shared pool for CPU-bound delegates.

Pool threads are a finite process resource. Long blocking operations can delay unrelated work, and thread-pool scheduling does not guarantee which thread will execute an item or when it will start. Code should therefore express dependencies through task completion rather than thread identity.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
