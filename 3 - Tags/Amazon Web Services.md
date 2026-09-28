# Amazon Web Services

Parent topic: [[Cloud Computing]]

Amazon Web Services is the chapter-level topic for the AWS global platform, its account and identity boundaries, core infrastructure and managed services, operational controls, economics, and adoption frameworks. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

Amazon Web Services turns the cloud model into a large service ecosystem whose parts can be assembled into business applications. The central architectural task is not memorizing product names. It is deciding where a workload should run, which responsibilities remain with the customer, how services communicate, what evidence shows that the design is secure and healthy, and how consumption remains aligned with business value. The provider supplies global facilities, managed control planes, APIs, and metered capacity; the customer chooses configurations and composes them into an application whose reliability, access, data protection, and cost still require deliberate engineering.

### Location, scope, and support

[[AWS Global Infrastructure and Support]] begins with the physical and logical scope of AWS services. A region is a geographically defined collection of infrastructure, while an availability zone is an isolated group of facilities within a region. Multi-zone deployment protects against a zone failure without assuming that a region is failure-free. Services may be global, regional, or zonal, and that scope determines where configuration and failure boundaries reside. Edge locations and regional edge caches bring content closer to users; Local Zones and Wavelength place selected capabilities near latency-sensitive workloads; Outposts extends AWS-managed infrastructure into customer sites. Support plans, health events, documentation, and technical resources provide different forms of operational assistance, but they do not replace the customer's own monitoring and response plans.

### Accounts and identity establish blast-radius boundaries

[[AWS Account Governance and Identity]] treats an AWS account as both a resource container and an isolation boundary. Separate accounts for development, testing, production, security, or sandbox use can limit accidental reach and make costs easier to attribute. AWS Organizations groups those accounts into organizational units, applies service control policies, and supports consolidated billing. Control Tower builds a governed multi-account landing zone from these mechanisms.

Within an account, IAM represents people, workloads, and services as principals whose permissions are evaluated from policies. Root-user credentials require exceptional protection, while roles provide temporary credentials that avoid distributing long-lived keys. Cross-account roles, Identity Center, Cognito, and Directory Service address different identity populations: organizational workforce, applications and customers, or directory-integrated users. Least privilege is a design process of granting only the required actions and resources, then checking actual use and revising access over time.

### Storage separates object, file, block, and transfer needs

[[Amazon S3 and Hybrid Storage]] distinguishes storage by access model rather than by a generic need to “save data.” Amazon S3 stores objects inside buckets with a globally unique namespace. Storage classes trade access cost, retrieval behavior, minimum duration, and resilience placement, while Intelligent-Tiering moves objects among access tiers when demand is uncertain. Bucket policies, encryption, versioning, replication, and lifecycle rules control who can access an object, how earlier states are preserved, where copies exist, and when data changes class or expires.

S3 can host static web content and accelerate long-distance transfers, but applications that need block or file semantics use different services. Storage Gateway connects on-premises workloads to cloud-backed file, volume, or virtual-tape interfaces. The Snow Family handles edge workloads and bulk movement when network transfer is unsuitable. These choices preserve the difference between an object's durable namespace, a shared filesystem, a virtual disk, and an offline transfer appliance.

### Networks express reachability and isolation

[[Amazon VPC and Hybrid Networking]] defines the network boundary in which many AWS resources run. A VPC receives an address range; subnets occupy particular availability zones; route tables decide where packets can travel. An internet gateway permits routed internet connectivity, while a NAT gateway lets instances in a private subnet initiate outbound connections without accepting unsolicited inbound sessions. Security groups apply stateful resource-level rules, and network ACLs apply stateless subnet-level rules.

VPC peering directly connects two networks without providing transitive routing. Transit Gateway uses a hub-and-spoke model when many VPCs and sites must communicate. Site-to-Site VPN crosses the public internet through encrypted tunnels, while Direct Connect supplies dedicated private connectivity. A bastion pattern provides controlled administrative entry, and a three-tier VPC design separates load balancing, compute, and databases so each layer has only the reachability it requires.

### Migration turns a portfolio into explicit disposition decisions

[[AWS Migration and Transformation Strategy]] separates moving workloads from transforming them. The seven migration strategies give each application a disposition: rehost it with minimal change, replatform selected infrastructure, refactor it around cloud-native capabilities, repurchase a replacement product, relocate an intact environment, retain it where it is, or retire it. Those decisions should follow discovery and readiness analysis rather than a blanket mandate to move everything the same way.

AWS organizes execution into assess, mobilize, and migrate-and-modernize phases. Assessment builds an inventory and business case; mobilization closes skills, governance, account, landing-zone, and dependency gaps; migration moves workload waves and then improves them. Application Migration Service, Application Discovery Service, Migration Hub, and the Migration Acceleration Program support different portions of that lifecycle. This makes migration a coordinated portfolio program whose technical move, organizational readiness, and modernization path remain distinguishable.

### Compute choices move the management boundary

[[AWS Compute and Serverless Services]] ranges from virtual machines to managed orchestration and functions. EC2 instances launch from machine images into hardware families selected for compute, memory, storage, or network characteristics. EBS supplies persistent block volumes, instance store provides host-attached temporary storage, EFS supplies a managed shared filesystem, and FSx offers managed filesystems such as Windows File Server.

On-Demand, Reserved, Spot, and dedicated options change the relationship among flexibility, commitment, interruption, isolation, and price. Lightsail packages common small-workload components. ECS manages containers, EKS provides managed Kubernetes, and Lambda runs functions in response to events without the customer managing servers. Higher abstraction reduces infrastructure administration but increases dependence on the service's execution and integration model.

### Managed databases match data shape and access pattern

[[AWS Managed Database Services]] separates relational transactions, key-value access, caching, warehousing, and migration. Amazon RDS manages relational engines and can place instances in subnet groups, automate backups, maintain a standby across zones, and add read replicas for read scaling. Aurora uses clustered storage across several zones and offers a serverless capacity mode.

DynamoDB supplies low-latency NoSQL access and can replicate multi-active tables across regions. ElastiCache places frequently used data in memory. Redshift serves analytical warehousing and can query data outside the warehouse through Spectrum. Database Migration Service moves and continuously replicates data, with schema conversion needed when source and target engines differ. These services reduce engine administration, yet schema design, credentials, recovery objectives, and query patterns remain application responsibilities.

### Availability uses health, distribution, and controlled elasticity

[[AWS Availability Scaling and Edge Delivery]] combines load balancing, auto scaling, DNS, and content delivery. Elastic Load Balancing checks targets and directs requests only to healthy capacity. Application, Network, and Gateway load balancers serve different protocol and appliance patterns. Auto Scaling Groups create or remove instances from launch templates according to desired capacity, schedules, measured targets, or step thresholds.

Route 53 holds DNS records in hosted zones and uses simple, weighted, latency, failover, geolocation, or geoproximity policies to answer queries according to design intent. Health checks can remove an unhealthy endpoint from eligible responses. CloudFront caches content at edge locations, while Global Accelerator improves the path to regional endpoints. These services improve resilience and reach only when origins, failover behavior, cache policy, and capacity rules are tested together.

### Events and analytics decouple work from data arrival

[[AWS Application Integration and Analytics]] connects independent components without requiring them to run at the same time. SNS publishes one message to several subscribers, SQS buffers work for later processing, and FIFO queues add ordering and deduplication constraints. Amazon MQ supports established broker protocols. EventBridge routes application and system events by rules, while Step Functions makes multi-stage workflow state and branching explicit.

Analytics services follow data from arrival to interpretation. Kinesis Data Streams retains ordered stream records for consumers; Data Firehose delivers streaming data to destinations; managed Flink processes streams. Glue discovers schema and catalogs datasets. Athena runs SQL over data in S3. OpenSearch provides low-latency search over logs or text, EMR runs large distributed data-processing frameworks, and QuickSight presents business intelligence. The correct tool follows ingestion rate, latency, structure, query style, and audience.

### Managed AI and automation create repeatable capabilities

[[AWS AI and Infrastructure Automation]] includes task-specific AI services and deployment tools. Rekognition analyzes images and video; Polly synthesizes speech; Transcribe produces text from audio; Translate converts languages; Textract extracts text and structure from documents; Comprehend analyzes language; SageMaker supports custom model building and operation. These services package complex capabilities behind APIs while leaving customers responsible for lawful data use and application decisions.

Elastic Beanstalk deploys application code onto managed infrastructure. CloudFormation describes resources in JSON or YAML templates and applies them as stacks, with change sets previewing updates. CodeCommit, CodeBuild, CodeDeploy, and CodePipeline support source, build, deployment, and delivery stages, while Amazon Q supplies generative assistance. Automation improves repeatability only when templates, artifacts, permissions, and change previews are versioned and reviewed.

### Platform engineering turns standards into reusable paths

[[AWS Cloud Operations and Platform Engineering]] treats operations as a designed system rather than a collection of console actions. A CloudOps model combines governance, compliance, provisioning, observation, and centralized operations. Service Catalog publishes approved products and portfolios, while AppRegistry associates resources with the applications, owners, and purposes they serve. Proton can expose standardized infrastructure and deployment templates to application teams without transferring every platform concern to them.

The Cloud Development Kit expresses infrastructure through reusable constructs that synthesize CloudFormation, and Amplify supplies an opinionated path for web and mobile delivery. Landing Zone Accelerator extends a secure multi-account baseline, while Systems Manager host management inventories and controls fleets. Together these mechanisms create paved roads: developers receive self-service interfaces, and platform teams retain versioned controls, ownership metadata, and operational visibility.

### Data engineering connects arrival, transformation, query, and ownership

[[AWS Data Engineering and Analytics Optimization]] follows data through a managed pipeline. MSK operates Apache Kafka workloads; Glue crawlers and jobs discover and transform datasets; EMR runs distributed frameworks; Redshift supplies a warehouse; Athena queries objects in place; QuickSight serves interactive analysis; and MWAA coordinates scheduled workflows. Serverless variants move capacity management to AWS when workload demand is intermittent or difficult to predict.

Optimization remains specific to each layer. Partition pruning reduces scanned data, workgroups separate Athena usage and controls, SPICE accelerates concurrent QuickSight analysis, and Spectrum extends Redshift queries into S3. DataZone adds discovery and governed sharing so datasets have visible producers, consumers, and business context. The result is not one monolithic analytics product but a chain whose schemas, partitions, schedules, ownership, performance, and costs must align.

### Generative AI joins model behavior to specialized infrastructure

[[AWS Generative AI and ML Infrastructure]] spans managed foundation-model APIs and the hardware beneath large training and inference workloads. Bedrock exposes multiple foundation models and adds guardrails, multi-agent collaboration, prompt routing, and prompt caching. These controls address different concerns: safety policy, task delegation, model selection, latency, and cost. They do not remove the need to evaluate output quality or control the data supplied to a model.

Trainium targets model training, while Inferentia targets inference. UltraCluster joins many accelerators with high-performance networking, and SageMaker HyperPod adds resilient large-scale training infrastructure. AWS Transform applies agentic assistance to modernization work. Selecting among these layers depends on whether a team wants a managed model API, a managed machine-learning workflow, or direct control over specialized distributed compute.

### Data lakes separate preservation, preparation, consumption, and governance

[[AWS Data Lake Architecture and Governance]] divides a lake into zones with distinct contracts. Raw storage preserves original inputs; landing performs initial checks; staging integrates and transforms; analytics organizes data for exploration; data marts curate business-specific subsets; and archive storage retains inactive history. The labels may vary, but separating these responsibilities makes retention, access, quality, and format transitions visible instead of allowing an S3 bucket to become an undifferentiated dump.

Lake Formation centralizes permissions and governed sharing around cataloged data. A lakehouse combines the scale and openness of a data lake with warehouse-like structure and query behavior, while a data mesh decentralizes ownership to domain teams under common governance. These are architectural choices about responsibility and access, not merely storage formats. A durable lake therefore joins physical zones to cataloging, lineage, quality controls, security policy, ownership, and cost-aware lifecycle management.

### Operations and security require continuous evidence

[[AWS Management and Observability]] makes workload condition and administrative change visible. CloudWatch collects metrics, builds dashboards, evaluates alarms, and stores logs. CloudTrail records management and data-plane API activity. AWS Config tracks resource configuration and evaluates rules. Systems Manager administers fleets through controlled capabilities, Trusted Advisor highlights selected risks and optimization opportunities, and AWS Health reports provider events that may affect resources.

[[AWS Security and Compliance]] frames this evidence within shared responsibility. AWS secures the cloud infrastructure; customers secure identities, configuration, applications, and data in the cloud according to the service model. Artifact provides compliance reports and agreements. KMS and CloudHSM address managed and dedicated key control, Certificate Manager supplies certificates, and Secrets Manager stores rotating application credentials. WAF filters web requests, Shield mitigates distributed denial-of-service attacks, Inspector identifies workload vulnerabilities, Macie discovers sensitive S3 data, GuardDuty detects suspicious activity, and Detective helps investigate relationships among findings. Layering matters because no single service covers prevention, detection, investigation, and recovery.

### Economics and frameworks connect architecture to outcomes

[[AWS Cloud Economics and Cost Management]] treats cloud cost as a consequence of architecture and consumption. Pay-as-you-go charging avoids a large initial hardware purchase but can become wasteful when idle resources or unsuitable pricing models persist. The Free Tier supports limited experimentation; Pricing Calculator estimates planned workloads; Migration Evaluator compares migration scenarios; Cost Explorer analyzes and forecasts actual spend. Cost-allocation tags attribute resources, Billing Conductor creates billing views, Budgets produces threshold alerts, and Savings Plans exchange commitment for discounted eligible use. Cost optimization is a continuous cycle of visibility, ownership, selection, and removal—not a one-time estimate.

[[AWS Cloud Adoption and Architecture]] supplies organizational and technical review structures. The Cloud Adoption Framework separates business, people, governance, platform, security, and operations perspectives so transformation includes culture, skills, controls, and operating models as well as migration. The Well-Architected Framework examines operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. The Well-Architected Tool records workload reviews, risks, and improvements over time. Frameworks do not choose services automatically; they make assumptions, tradeoffs, ownership, and evidence explicit enough to revisit.

Together, these topics describe AWS as a set of bounded managed capabilities rather than one undifferentiated cloud. Strong designs align service scope, account boundaries, identity, network reachability, data semantics, compute abstraction, failure handling, event flow, observability, security responsibility, and cost. The service catalog will change, but those relationships remain the durable basis for selecting and operating AWS solutions.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Amazon Web Services]]"
```
