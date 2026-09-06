2026-09-06 00:13

Status: #baby

Tags: [[Search Algorithms]]

# Secretary Problem

The secretary problem is an [[Optimal Stopping Problem]] in which candidates arrive one at a time, must be accepted or rejected immediately, and cannot be revisited. The objective is to maximize the probability of choosing the best candidate.

For $n$ randomly ordered candidates, the strategy first observes and rejects roughly the initial $n/e$, using their best member as a benchmark. It then selects the first later candidate better than that benchmark. The method succeeds in about $1/e$, or 37 percent, of cases, and no competing rule has a higher probability under these assumptions.

# References

[[algorithms.epub]]
