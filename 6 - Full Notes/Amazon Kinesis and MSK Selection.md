2026-09-27 20:01

Status: #baby

Tags: [[AWS Data Engineering and Analytics Optimization]]

# Amazon Kinesis and MSK Selection

Amazon Kinesis Data Streams and Amazon MSK both carry streaming records, but they preserve different ecosystems. Kinesis offers an AWS-native stream model and close integration with AWS services, while MSK preserves Kafka protocols, client libraries, and tooling. Existing Kafka skills or portability needs favor MSK; simpler AWS-native integration can favor Kinesis. Throughput, retention, partition operations, consumer patterns, and operating responsibility should drive the choice rather than the generic label “streaming.”

# References

[[awsforsolutionsarchitectsthirdedition.pdf]]

