2026-09-27 11:43

Status: #baby

Tags: [[C Sharp Code Quality Metrics and Static Analysis]] [[Software Design Principles]]

# Class Coupling

Class coupling measures the number of other types a class directly depends on through parameters, fields, return types, inheritance, calls, or construction. Broad coupling increases the number of changes that may affect the class and the setup needed to test it.

The goal is purposeful dependency, not zero dependency. Stable abstractions and cohesive collaborators can be reasonable, while unrelated knowledge gathered into one class signals a boundary that deserves review.

The source connects loose coupling to the [[Principle of Least Knowledge]]: a class should collaborate directly with as few other classes as its responsibility requires and should ask an immediate collaborator to perform work instead of navigating through that collaborator's internal objects.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]
