2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Thread-Local and Partition-Local State

Thread-local state gives each participating thread a private value, while partition-local overloads let a parallel operation initialize, update, and finally combine state associated with a work partition. Both reduce repeated contention on one shared accumulator.

The final merge still needs a correct combining operation, and code should not assume that one logical task always remains on a particular thread. Partition-local state better matches algorithms whose partial results can be reduced independently.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
