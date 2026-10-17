2026-10-16 23:18

Status: #baby

Tags: [[Symmetry-Equivariant Variational Quantum Learning]]

# Lie-Algebra Criterion for Equivariant Quantum Embeddings

Suppose a linear encoding maps data into a quantum generator as $U(x)=e^{-iE(x)}$, and a continuous symmetry acts on the data through $V_s=e^G$. A compatible unitary $U_s=e^H$ exists when the encoded data subspace transforms under quantum conjugation in the same way as the original data space, summarized infinitesimally by $EG=\operatorname{ad}_H E$.

Equivalently, the adjoint representation of the quantum Lie algebra must contain a subrepresentation identical to the symmetry representation acting on the data. Merely finding an isomorphic subalgebra is insufficient; the action on the image of $E$ must match.

The criterion explains the success of [[SO(3)-Equivariant Quantum Embedding]] and also its limits. A useful continuous data symmetry must admit an appropriate finite-dimensional unitary representation, and every symmetry has the uninformative fallback $E=0$, which is equivariant but encodes no data.

# References

[[2022 - Exploiting symmetry in variational quantum machine learning.pdf]]

