2026-10-30 16:54

Status: #baby

Tags: [[Java Collection and Stream Evolution]]

# Java Reversed Collection View

A Java sequenced collection's `reversed()` operation returns a reverse-order view rather than an independent copied collection. Iterating the view begins at the original collection's last element and proceeds toward its first.

Because the two structures are views of the same data, supported changes through either side are reflected in the other. This is efficient and preserves end semantics, but callers must not assume the reversed result is a detached snapshot.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
