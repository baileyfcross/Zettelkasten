2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Interfaces Generics and Inheritance]]

# Generic Variance

Generic variance describes when constructed generic interfaces or delegates remain assignment-compatible across an inheritance relationship. Covariance marks an output type parameter with `out`, while contravariance marks an input type parameter with `in`.

The direction reflects how the parameter is used: a covariant producer can supply a more derived result, and a contravariant consumer able to accept a base type can also accept values supplied through a more specific contract.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

