2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring GraphQL ArgumentValue Partial Update

Spring GraphQL `ArgumentValue<T>` preserves the difference between a mutation input that was omitted and one that was explicitly supplied as null. Its presence flag answers whether the client included the field, while its value carries the supplied value, including null.

That distinction enables PATCH-like mutations. An omitted company name means retain the stored value; an explicitly null name can mean clear it when the schema permits null. A plain nullable Java parameter cannot express both states, so using the wrapper prevents an update mapper from erasing data merely because a client did not mention a field.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
