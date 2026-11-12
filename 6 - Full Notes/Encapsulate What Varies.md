2026-11-11 18:27

Status: #baby

Tags: [[Software Design Principles]]

# Encapsulate What Varies

Encapsulate what varies is the design principle of separating likely change from stable behavior. The variable decision is placed behind a class or interface so new alternatives can be introduced without repeatedly modifying the code that uses the result.

The boundary should correspond to an observed reason for change, not a speculative abstraction for every possibility. The source's playing-style example keeps a musician's stable responsibilities separate from interchangeable style behavior, protecting the stable code from each new variation.

# References

[[softwaredevelopmentdesignandcoding_withpatternsdebuggingunittestin.epub]]

