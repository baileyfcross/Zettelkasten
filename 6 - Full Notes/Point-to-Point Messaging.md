2026-09-09 00:00

Status: #baby

Tags: [[Cloud Integration and Messaging]]

# Point-to-Point Messaging

Point-to-point messaging addresses a message to a particular receiver or set of intended receivers. It is suitable when one known participant should perform the work rather than every subscriber interested in a topic.

The queue or messaging system still needs access controls and delivery rules. [[Broadcast Message|Broadcast messaging]] uses the contrasting pattern in which interested receivers subscribe to a common topic or event.

In the AWS microservice discussion, an SQS queue implements point-to-point work distribution: several workers may poll the queue, but one successful consumer processes and removes a given message. This differs from an SNS topic, where each subscription receives its own copy and can process the event independently.

# References

[[cloudcomputing_mit.epub]]

[[awsforsolutionsarchitectsthirdedition.pdf]]
