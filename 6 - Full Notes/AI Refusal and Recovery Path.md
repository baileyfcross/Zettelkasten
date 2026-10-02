2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Responsible AI Controls]]

# AI Refusal and Recovery Path

An AI refusal and recovery path specifies what the system should do when it cannot safely, lawfully, or reliably complete a request. A useful refusal states the boundary without exposing sensitive policy details, avoids fabricating an answer, and directs the user toward a permitted reformulation, approved source, or human escalation channel.

Recovery is important because a bare rejection can leave legitimate users stranded. Teams should test whether the system distinguishes prohibited requests from incomplete or ambiguous ones, offers safe alternatives, and preserves context during escalation. Refusal quality belongs in evaluation datasets alongside ordinary task success rather than being treated as an exceptional afterthought.

# References

[[microsoftfoundryinaction.pdf]]
