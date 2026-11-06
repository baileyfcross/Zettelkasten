2026-11-06 13:25

Status: #baby

Tags: [[Sorting Algorithms]]

# External Sorting

External sorting orders a dataset that does not fit in available memory by dividing it into manageable chunks. Each chunk is sorted in memory and written as an ordered run; the runs are then merged into a final ordered result.

The merge phase follows the same central operation as [[Merge Sort]]: because each input run is already ordered, the algorithm repeatedly selects the next smallest available item. This makes merge-based sorting suitable for large logs, batch jobs, and distributed processing in which partitions are sorted separately.

The design trades disk or network input/output and temporary storage for the ability to process data larger than RAM. Predictable $O(n\log n)$ comparison work and stable merging can be more important than the in-memory locality of [[Quicksort]].

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
