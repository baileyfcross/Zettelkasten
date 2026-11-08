2026-11-06 13:52

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Two-Phase Commit Protocol

Two-phase commit coordinates one atomic decision across multiple transactional resource managers. In the voting phase, the coordinator asks each participant to durably prepare and report whether it can commit. In the completion phase, the coordinator tells every participant to commit if all voted yes, or to abort otherwise.

The protocol supplies a stronger cross-resource guarantee than independent local commits, but it adds coordinator round trips and keeps resource locks longer. A prepared participant or coordinator failure can also delay completion for an unbounded period even when recovery eventually resolves the transaction. It is therefore a contextual tool rather than a default microservice mechanism: local transactions, [[BASE Transaction]], or [[Saga Transaction]] can be preferable when availability and scalable partitioning matter more than instantaneous cross-service atomicity.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
