2026-09-06 19:44

Status: #baby

Tags: [[Matrix Invertibility and Factorization]]

# Banded Matrix

A banded matrix concentrates its possible nonzero entries in a limited set of diagonals around the main diagonal. Its bandwidth records how many of those diagonals may contain nonzero values.

Banded structure reduces storage and arithmetic because operations can ignore known zeros. A [[Tridiagonal Matrix]] is the important case with only the main diagonal and its two neighboring diagonals.

Algorithms should store and traverse only the active diagonals rather than apply a dense matrix routine to explicit zeros. A derived matrix representation can reuse general operations while specializing multiplication or factorization to preserve the storage and speed advantages of the band.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
