2026-11-11 18:27

Status: #baby

Tags: [[Software Design Principles]]

# Composition over Inheritance

Composition over inheritance favors assembling behavior from collaborating objects when a subclass is not genuinely substitutable for its base class. Delegation lets one object hand a responsibility to another, while composition and aggregation express whole-part relationships with different ownership expectations.

These alternatives reduce dependence on a superclass's implementation and allow behavior to vary independently. Inheritance remains appropriate for a true is-a relationship that satisfies the [[Liskov Substitution Principle]]; composition is not a ban on inheritance but a safer default for sharing changeable behavior.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

