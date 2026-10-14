2026-10-14 01:16

Status: #baby

Tags: [[JavaScript Core Semantics]]

# JavaScript Prototype Delegation

JavaScript prototype delegation is the fallback lookup that occurs when an object does not contain a requested property. The engine follows the object's internal prototype link to another object and continues the search there.

`Object.create(source)` can create a new object linked to `source`, allowing the new object to use behavior or data it does not own directly. The source presents this as behavior delegation: linked objects deliberately share responsibilities, a model distinct from pretending that the prototype mechanism is classical inheritance.

# References

[[youdontknowjs_upandgoing.pdf]]
