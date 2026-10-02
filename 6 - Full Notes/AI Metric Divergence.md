2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# AI Metric Divergence

AI metric divergence occurs when operational and behavioral signals move in different directions. Latency and error rates may remain stable while groundedness declines, or response quality may improve while token use and cost become unsustainable. Treating either signal family as a complete health measure can therefore conceal material degradation.

Divergence is diagnostically useful because it narrows the likely cause. Stable infrastructure with worsening quality points toward data, prompts, models, or agent behavior; worsening latency with stable quality points toward capacity or execution. Monitoring should surface these combinations and connect them to versions, traffic changes, and recent configuration changes.

# References

[[microsoftfoundryinaction.pdf]]
