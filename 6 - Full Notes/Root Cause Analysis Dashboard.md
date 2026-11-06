2026-11-06 12:32

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Root Cause Analysis Dashboard

A root cause analysis dashboard presents correlated operational evidence as a cause-and-effect story rather than as an inventory of unrelated charts. It starts with the affected business flow and lets a responder follow identifiers, traces, errors, releases, entities, resources, profiles, and system activity through the layers that processed the transaction.

The dashboard is a query surface over a [[Root Cause Analysis Data Model]]. Joins and lookups can place several trace identifiers in chronological order under one order or payment identifier, connect a span to a log or profile, and expose a deployment or infrastructure condition beside the observed latency. Broken navigation is itself evidence that a required signal or correlation is missing.

A small number of coherent dashboards is easier to operate than many unstandardized panels. An RCA overview should establish context and provide links into business- or component-specific dashboards whose service objectives reflect the responsibilities of that layer. This preserves a common investigative path while allowing frontend, API, messaging, database, batch, and legacy systems to expose different health measures.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
