2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon DB Client Metrics

Helidon DB Client metrics are interceptor services that count or time selected database activity. A metric can be restricted to particular named statements or statement types and can measure successful executions, failed executions, or both.

The example counts `select-all` and `select-one` statements while timing delete, update, and insert types. Attaching those services to the client builder makes the resulting measurements available through the application's metrics facilities without changing each CRUD handler.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
