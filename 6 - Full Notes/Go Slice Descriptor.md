2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Slice Descriptor

A Go slice is a variable-length view over a backing array. Conceptually it carries a reference to array storage together with a current length and a capacity, so two slices can expose overlapping regions of the same data.

Changing an element through one shared view is visible through the other. Reslicing changes the visible range without necessarily copying data, while growth beyond capacity can move one slice to a new backing array and end that sharing relationship.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
