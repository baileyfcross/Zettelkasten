2026-09-16 00:29

Status: #baby

Tags: [[Functions and Elementary Number Theory]] · [[Functions Cardinality and Relational Data]] · [[Function Analysis and Transformations]] · [[Functional JavaScript Programming]]

# Function Composition

Function composition applies one function and then another, with (g ◦ f)(x) = g(f(x)). Composition is associative when the domains and codomains match.

Automorphisms form groups under composition because identities and inverse functions preserve the structure.

Composition is defined when the outputs of the first function lie in the domain of the second. Its associativity allows a chain of transformations to be grouped without changing the resulting mapping.

In functional JavaScript, a composition helper accepts several functions and returns one function that sends an initial argument through them in sequence. An implementation can use [[JavaScript Array Reduce|reduce]] or `reduceRight`, so the library's direction convention matters: the output of each step becomes the input of the next.

# References

[[essentialsofmodernalgebra.pdf]]

[[FoundationsOfComputation_2.3.2.pdf]]

[[foundationsofmath.pdf]]

[[learningreact1.pdf]]
