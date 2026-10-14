2026-09-08 21:16

Status: #baby

Tags: [[.NET Task Parallelism and Asynchrony]] [[Linux Process and Task Internals]]

# Process Thread and Task

A process is an executing program with its own resources, a thread is an operating-system execution path within that process, and a .NET task is a higher-level representation of work or a future result. Tasks allow application code to express dependencies and completion without directly managing every thread.

A task does not always imply a newly created thread. It may run on a thread-pool worker, represent asynchronous I/O that uses no thread while waiting, or complete synchronously when its result is already available.

The source also distinguishes multitasking among processes from multithreading inside one process. Parallel programming is the narrower case in which useful computations actually overlap, usually to exploit several processor cores.

In Linux, the scheduler operates on threads as [[Kernel Schedulable Entity|kernel schedulable entities]]. Each thread has its own [[Linux Task Structure]] and stacks, while threads in one process can share the user address space and other resources; their common [[Thread Group ID]] preserves the user-visible process relationship.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
[[linuxkernelprogramming_secondedition.pdf]]
