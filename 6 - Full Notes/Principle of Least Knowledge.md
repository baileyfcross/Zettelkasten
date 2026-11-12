2026-11-11 18:27

Status: #baby

Tags: [[Software Design Principles]]

# Principle of Least Knowledge

The Principle of Least Knowledge, also called the Law of Demeter, asks an object to communicate with a small set of immediate collaborators rather than navigating through chains of their internal objects. The rule limits how much of the surrounding object graph one method must understand.

When a caller reaches through several objects to obtain a value, a change to any intermediate relationship can break the caller. Asking the nearest collaborator for the needed result preserves [[Information Hiding]] and reduces [[Class Coupling]].

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

