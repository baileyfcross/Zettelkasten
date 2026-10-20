2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Interface Composition

Go composes an interface by embedding other interfaces in its declaration. The resulting method set is the union of the embedded methods plus any methods declared directly by the new interface.

Identical embedded signatures collapse to one requirement, while methods with the same name but incompatible signatures make the composition invalid. Small interfaces can therefore be combined for a consumer that needs several behaviors without forcing every user to depend on the larger contract.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
