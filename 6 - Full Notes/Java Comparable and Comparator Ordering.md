2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Comparable and Comparator Ordering

`Comparable<T>` places a natural ordering inside the compared type through `compareTo`. `Comparator<T>` defines an ordering externally, allowing the same type to be sorted by different properties or to avoid owning the comparison policy.

A comparison returns a negative, zero, or positive result rather than a distance. Sorted collections treat comparison equality as the basis for uniqueness, so an ordering that is inconsistent with `equals` can produce surprising set or map behavior. Comparator composition can add secondary keys when the primary comparison ties.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
