2026-09-30 22:58

Status: #baby

Tags: [[Microsoft Entra Governance and Protection]]

# Microsoft Entra Lifecycle Workflow

A Microsoft Entra Lifecycle Workflow automates identity tasks around joiner, mover, and leaver events. A workflow combines an execution trigger, a scoped population, and ordered tasks such as adding or removing groups, enabling or disabling accounts, sending notifications, or removing licenses.

Triggers can depend on time-based employee attributes, attribute changes, group membership changes, inactivity, or an on-demand run. Scheduled execution and history make the automation observable, while versions preserve what changed between runs. The workflow reduces delay and manual inconsistency, but its scope and source attributes must be trustworthy: an incorrect hire date, manager, or termination signal can automate the wrong access change at scale.

# References

[[masteringmicrosoftentraid.pdf]]
