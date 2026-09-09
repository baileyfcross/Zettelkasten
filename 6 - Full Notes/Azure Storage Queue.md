2026-09-08 22:09

Status: #baby

Tags: [[Azure Blob and Queue Storage]]

# Azure Storage Queue

An Azure Storage Queue holds messages that producers add and independent workers retrieve. The order-processing project uses a queue to distribute sales orders among replicated microservice instances without binding a producer to one worker.

The book chooses storage queues because strict delivery order is not required. A worker reads and deserializes a message, performs its work, and removes the message, so deletion timing must account for crashes that could otherwise lose uncompleted work.

# References

[[c8andnetcore30projectsusingazure.pdf]]
