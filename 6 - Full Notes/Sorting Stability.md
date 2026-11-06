2026-11-06 13:25

Status: #baby

Tags: [[Sorting Algorithms]]

# Sorting Stability

Sorting stability means that records with equal sort keys retain their original relative order. This property matters when the earlier order carries meaning or when records are sorted successively by multiple keys.

[[Merge Sort]] can be stable when the merge operation takes an equal-key item from the left input before its counterpart from the right. Classical in-place [[Quicksort]] is not stable because partition swaps can reverse equal-key records.

Stability is therefore an algorithm-selection constraint rather than an incidental implementation detail. A method with attractive average runtime may be unsuitable when equal-key order must be preserved.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
