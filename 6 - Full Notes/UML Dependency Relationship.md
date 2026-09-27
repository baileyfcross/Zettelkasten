2026-09-26 22:56

Status: #baby

Tags: [[Object-Oriented Structural Modeling]]

# UML Dependency Relationship

A UML dependency says one element uses or relies on another without necessarily retaining it as part of its structure. It is conventionally shown as a dashed directed line pointing toward the supplier.

A method parameter or temporary collaborator can create this relationship: changes to the supplier's contract may affect the dependent client, even though their instances do not share a whole-part lifetime. This distinguishes dependency from a stored [[UML Association Relationship|association]].

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

