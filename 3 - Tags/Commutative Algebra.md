# Commutative Algebra

Parent topic: [[Mathematics]]

Commutative Algebra is the chapter-level topic for rings, ideals, modules, local and graded structure, homological methods, and their applications to polynomial equations and algebraic geometry. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

Commutative algebra studies algebraic systems in which multiplication is commutative and an identity element is available. Its basic objects are rings, ideals, and modules. A ring supplies addition and multiplication, an ideal records a collection stable under ring multiplication, and a quotient ring turns every element of that ideal into zero. These constructions make systems of polynomial equations accessible through algebra: instead of following each equation separately, one studies the ideal they generate and the structural properties that remain unchanged under valid transformations.

### Rings, ideals, and finiteness

[[Ring and Ideal Foundations]] begins with the relationships among fields, integral domains, units, zero divisors, nilpotent elements, ideals, homomorphisms, and quotients. A field makes every nonzero element invertible, while an integral domain merely rules out zero divisors. Ideals are simultaneously additive substructures, kernels of homomorphisms, and the data needed to form quotient rings. The first isomorphism theorem explains why the image of a ring homomorphism is represented by the source modulo its kernel.

[[Prime Ideals and Noetherian Algebra]] identifies ideals that control factorization and decomposition. A prime ideal produces an integral-domain quotient, and a maximal ideal produces a field quotient. Radicals forget multiplicity while retaining the prime support of an ideal. The nilradical collects all nilpotent elements; the Jacobson radical intersects all maximal ideals. Noetherian conditions replace potentially infinite ascending behavior with finite generation, allowing ideals to be decomposed into finitely many primary pieces whose radicals are prime.

### Localizing algebra

[[Localization and Local Algebra]] changes which elements are invertible. Given a multiplicatively closed set, localization forms fractions whose denominators come from that set and satisfies a universal property: any homomorphism already making those denominators invertible factors uniquely through the localization. Ideals extend to the localized ring and contract back to the original ring, while prime ideals that meet the denominator set disappear.

Localization at the complement of a prime ideal creates a local ring with one maximal ideal. This converts a global problem into a neighborhood of one prime and makes many properties testable point by point. Localization is exact on modules and is compatible with quotients. Saturation expresses a related operation algebraically by collecting elements that enter an ideal after multiplication by a sufficiently high power of another ideal.

### Polynomial computation and geometry

[[Polynomial Algorithms and Elimination]] connects the structural theory to explicit calculation. Division in one variable yields principal ideals and Bézout identities for coprime polynomials. Sylvester matrices and resultants detect common factors. Hilbert's basis theorem guarantees finite generation for polynomial ideals over Noetherian rings. In several variables, a monomial order selects leading terms, and a Gröbner basis makes the leading ideal finitely manageable. Buchberger's algorithm constructs such a basis using reductions of S-polynomials.

Elimination chooses an order that removes designated variables. The polynomials in a Gröbner basis that avoid those variables form a basis for the corresponding elimination ideal. This turns projection, ideal membership, and implicit equation problems into finite computations, although the cost depends heavily on the monomial order and the size of intermediate expressions.

[[Affine Geometry and Schemes]] interprets the same algebra geometrically. An affine variety is a common zero set of polynomials, while its vanishing ideal contains all polynomials that vanish on it. Projection can fail to produce a closed algebraic set, so elimination naturally returns its Zariski closure. Polynomial and rational implicitization replace a parametrization with equations defining the closure of its image.

The spectrum of a ring takes prime ideals as points and equips them with the Zariski topology. A structure sheaf assigns localized rings to open regions, so functions can be described locally and compared through restriction. Presheaves, sheaves, stalks, quasi-coherent sheaves, and locally ringed spaces extend the correspondence between rings and geometric spaces. An affine scheme packages a spectrum with its structure sheaf, while modules over the ring correspond to quasi-coherent sheaves on that scheme.

### Modules and exactness

[[Module Structure and Exact Sequences]] generalizes linear algebra from vector spaces over fields to modules over rings. Submodules, quotients, direct sums, free modules, and homomorphism modules provide the basic operations. The annihilator records which scalars kill a module, and faithfulness means no nonzero scalar kills every element. Nakayama's lemma shows how finite generation and the Jacobson radical control whether a proposed generating set is sufficient.

Exact sequences express how kernels and images fit together. A short exact sequence identifies one module as a submodule and another as the resulting quotient; when it splits, the middle module is a direct sum. Commutative diagrams make compatibility among several maps visible. The Four Lemma, Five Lemma, and Snake Lemma transfer injectivity, surjectivity, and kernel-cokernel information across related exact rows.

[[Projective Flat and Injective Modules]] studies modules by how they preserve or lift maps. Projective modules lift homomorphisms across surjections and are direct summands of free modules. Injective modules extend maps across injections. Resolutions replace a module by a linked sequence of projective, free, or injective modules so that derived invariants can be computed.

Tensor products represent bilinear maps universally and support extension of scalars. A flat module is one whose tensor product preserves exact sequences; faithful flatness also detects exactness. Localization is a central flat construction. Finite presentation and localization together provide a local test for projectivity: under the required finiteness conditions, a module is projective precisely when its localizations are free.

### Primes, decomposition, and dimension

[[Associated Primes and Module Dimension]] links individual elements of a module to prime ideals through annihilators. Associated primes locate the module's essential algebraic support, while embedded primes record nonminimal components. Primary modules and primary submodules isolate behavior attached to a single prime, and primary decomposition expresses a submodule as an intersection of these components.

Length and dimension measure different kinds of size. A finite composition series counts simple factors, and finite length is equivalent to being both Noetherian and Artinian. Krull dimension is determined by chains of prime ideals; the height of a prime measures chains below it. A module inherits dimension from the quotient by its annihilator, connecting support, prime chains, and local algebra.

### Grading, filtration, and growth

[[Graded Algebra and Hilbert Theory]] decomposes rings and modules into homogeneous degree pieces. Homogeneous ideals and maps respect those pieces, while degree shifts reposition them without changing their algebraic relationships. Graded localization preserves degree information, and the graded form of Nakayama's lemma identifies minimal homogeneous generators.

A filtration instead records nested approximation levels. Its associated graded ring separates successive layers, while the Rees algebra stores every power of an ideal in one graded object. The Artin-Rees lemma controls how an ideal-power filtration meets a submodule, and Krull's intersection theorem describes what survives every power. Hilbert functions and series count graded pieces; eventual polynomial behavior connects this growth to dimension and multiplicity.

[[Regular Sequences and Syzygies]] studies equations whose successive elements remain non-zero-divisors. Systems of parameters reduce a local module to finite length, while regular systems of parameters characterize regular local rings. Complete intersections are generated by regular sequences of the expected length. Quasi-regular sequences capture a related condition through the associated graded structure.

Syzygies are relations among generators. A presentation matrix records first syzygies, and a free resolution continues by finding relations among relations. Minimal graded resolutions expose graded Betti numbers and projective dimension. Hilbert's syzygy theorem bounds the length of a graded free resolution over a polynomial ring, and Castelnuovo-Mumford regularity summarizes how far generator and relation degrees extend beyond their homological positions.

### Homological methods

[[Homological Algebra and Derived Functors]] organizes modules into complexes whose consecutive maps compose to zero. Cycles and boundaries form homology groups, while cocomplexes produce cohomology. A short exact sequence of complexes generates a long exact sequence in homology, allowing information to pass between linked complexes.

Tor measures the failure of tensor product to preserve exactness and characterizes flat modules through vanishing. Ext is built from projective or injective resolutions and measures higher extension behavior beyond ordinary Hom. Koszul complexes encode a sequence of ring elements through exterior powers; their homology detects regularity. Depth is the length of a maximal regular sequence, and the Auslander-Buchsbaum formula balances depth against finite projective dimension over a Noetherian local ring.

[[Local Cohomology and Rees Algebra]] gathers the later structural and computational tools. Regular rings remain regular after localization, and determinantal ideals measure the rank of maps between free modules. McCoy's theorem and the Buchsbaum-Eisenbud criterion turn determinant, rank, and depth conditions into tests for nontrivial solutions and exact complexes.

Local cohomology is derived from sections annihilated by powers of a chosen ideal. It can be calculated through a Čech complex of localizations, behaves functorially under change of rings, and participates in Mayer-Vietoris sequences. Fitting ideals summarize a module through minors of a presentation matrix and commute with base change. Symmetric and Rees algebras compare formal products of ideal generators with their actual products; ideals of linear type are precisely those for which this comparison has no extra kernel. Approximation complexes and double Koszul constructions use these relationships to study implicit equations, regularity, and resultants.

Across these topics, commutative algebra moves repeatedly between global and local, equations and geometry, generators and relations, and concrete computation and abstract invariants. A choice such as localization, grading, or resolution does not discard the original object; it exposes one aspect in a form that can be measured. The resulting theory is cumulative: finite generation makes decomposition possible, localization reveals pointwise behavior, homological methods measure failures of exactness, and geometric interpretations explain why those algebraic measurements matter.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Commutative Algebra]]"
```
