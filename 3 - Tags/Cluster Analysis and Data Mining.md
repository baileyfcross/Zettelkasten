# Cluster Analysis and Data Mining

Parent topic: [[Computer Science]]

Cluster Analysis and Data Mining is the chapter-level topic for finding structure in data, assigning observations to meaningful groups, validating those structures, and interpreting their limits. Full Notes should link to a focused child topic rather than directly to this chapter tag.

## Overview Chapter

Cluster analysis begins with a deceptively simple objective: place similar objects together and dissimilar objects apart. The difficulty lies in deciding what similarity means, which attributes deserve influence, how many groups the data support, and whether the resulting structure reflects anything beyond the behavior of a chosen algorithm. Data mining places this problem inside a larger discovery process. The analyst must understand the application, prepare and explore the data, select a model, evaluate the result, and decide how discovered patterns will be used. A cluster is therefore not a fact extracted mechanically from a database. It is a model produced by an explicit chain of representational, computational, and interpretive choices.

### Defining the clustering problem

[[Cluster Analysis Foundations]] treats a cluster as a class inferred from the data rather than supplied in advance. Objects within a cluster should be homogeneous with respect to the selected features, while objects in different clusters should be well separated. Crisp clustering assigns each object to one group. Overlapping and fuzzy approaches relax that exclusivity. In every case, the number, shape, scale, and meaning of clusters depend on the operational definition of proximity and the objective used to judge a proposed grouping.

A clustering workflow first represents each object through attributes, computes pairwise proximity, and applies a grouping method. A proximity measure may express similarity, where larger values indicate stronger resemblance, or dissimilarity, where smaller values indicate nearness. Euclidean distance emphasizes straight-line geometry; Manhattan distance accumulates coordinate differences; other Minkowski, Chebyshev, power, or disagreement measures create different neighborhood shapes. An epsilon neighborhood groups points lying within a specified radius, but one choice of metric or radius can join structures that another choice separates. Robust work therefore compares plausible representations and measures rather than treating one output as uniquely correct.

A proximity matrix records pairwise relationships and provides the input for many algorithms. A dendrogram visualizes a hierarchy by showing when objects or clusters join. A horizontal cut through that tree proposes one partition, but the cut level is a modeling decision. Visualizations help expose separation, overlap, density variation, and suspicious points that a summary statistic can conceal. They do not replace validation; they make the assumptions and consequences of an analysis easier to inspect.

### Discovery as a process

[[Data Mining Process and Infrastructure]] places algorithms inside a repeatable knowledge-discovery cycle. Data mining extracts patterns such as clusters, classifications, associations, sequences, correlations, trends, and predictive models. Knowledge Discovery in Databases is broader: it begins with application goals and ends with interpreted knowledge incorporated into practice. The nine-step KDD model repeatedly moves among understanding, selection, cleaning, reduction, method and algorithm choice, mining, interpretation, and deployment.

CRISP-DM expresses a related industrial workflow through business understanding, data understanding, preparation, modeling, evaluation, and deployment. Both frameworks are iterative because an unexpected model often reveals a defect in the data or a misunderstanding of the goal. Model evaluation is not a final ceremonial check. It can send the project back to attribute construction, sampling, or even the original business question.

The infrastructure matters as much as the algorithm. A data warehouse integrates subject-oriented, time-varying organizational data for decision support; a data mart narrows that repository to one subject area. Multidimensional databases and data cubes support slicing, pivoting, filtering, drill-down, and other exploratory operations through online analytical processing. Exploratory data analysis and visualization help the analyst understand distributions and relationships before modeling. Rule induction and deployment then turn patterns into operational behavior. Throughout the process, the analyst must understand the domain represented by the database, not merely the software used to query it.

### Nested versus single-partition solutions

[[Hierarchical Clustering Methods]] creates a family of nested groupings. Agglomerative methods begin with singleton objects and merge the most compatible pair at each step. Divisive methods begin with all objects together and split clusters until a stopping condition is met. Once an agglomerative merge occurs it is permanent, which makes early choices structural building blocks for every later level.

Linkage rules define the distance between clusters. Single-link clustering uses the nearest cross-cluster pair and can connect elongated chains. Complete-link clustering uses the most distant cross-cluster pair and tends to favor compact groups. Centroid linkage compares representative centers. Ward's method merges the pair that produces the smallest increase in an error sum-of-squares objective. Homothetic divisive methods split through one binary variable, while polythetic methods use the full attribute set. The cophenetic proximity records the level at which two observations first share a cluster, connecting the numerical hierarchy to its dendrogram.

[[Partition and K-Means Clustering]] seeks one partition rather than an entire tree. Iterative methods begin from seeds or an initial assignment, compute representative centers, reassign poorly fitting objects, and repeat until membership stabilizes. K-means minimizes within-cluster squared error around centroids. MacQueen's variant updates centroids as individual objects move, while Forgy's method holds centers fixed for a full allocation pass and then recomputes them. Jancey's method repeatedly reallocates objects using class points derived from the old center and the new centroid.

These methods are efficient but initialization-sensitive. A run can converge to a local optimum without revealing whether a better global solution exists, so analysts commonly repeat it from distinct starting configurations. K-means also favors roughly spherical groups and can be distorted by noise, outliers, unequal sizes, and unequal densities. BIRCH addresses large numerical databases with a height-balanced cluster-feature tree. Compact triples store the number, linear sum, and squared sum of points; a later partitioning phase clusters the leaf summaries. This reduces memory and scan costs, but input order, thresholds, and the same preference for compact clusters still affect the result.

### Capturing judgment and partial membership

[[Judgmental Analysis]] applies regression and hierarchical grouping to decision policies. Each judge rates a common collection of profiles described by predictor variables. A multiple-regression equation captures how consistently that judge combines the predictors, and its squared multiple correlation measures predictive efficiency. JAN then merges the two most similar policy equations at each stage, choosing the merge that produces the smallest loss of overall predictive efficiency.

The resulting hierarchy can reveal one shared policy or several policy groups. Ipsative analysis lets judges draw on personal knowledge of the cases; normative analysis directs them to the supplied predictors. Type A studies use the same subjects for every judge, whereas Type B studies allow different judged subjects. The Kelley-Salisbury iteration estimates regression weights without directly solving the normal equations. The cutoff can be chosen through an F test, a sharp loss in predictive efficiency, or a predefined threshold. The method turns subjective ratings into inspectable equations while preserving evidence of disagreement rather than averaging it away prematurely.

[[Fuzzy Clustering]] addresses boundaries that are not naturally crisp. A fuzzy set assigns each object a membership value between zero and one. An object can therefore belong partly to several clusters, and a membership matrix records those degrees. A fuzzy cluster center is a membership-weighted representative, while an objective function evaluates the weighted distances between points and centers.

Fuzzy C-means alternates between recomputing centers and updating memberships until successive membership matrices change by less than a tolerance. Probabilistic formulations require memberships for each point to sum to one, making them partition-like. Possibilistic formulations relax that constraint and treat membership as the degree to which a point exemplifies a cluster independently of other clusters. Membership functions can be triangular, trapezoidal, Gaussian, or sigmoidal. These models express gradual categories and overlapping structure, but they introduce design choices and computational complexity; a crisp method remains preferable when it represents the application adequately.

### From discovered groups to predicted classes

[[Classification and Decision Trees]] begins where cluster discovery ends. In supervised classification, classes and training labels are known, and the goal is to learn a model that assigns unseen records to those classes. The workflow separates model construction, evaluation, and application. Accuracy on held-out or pilot data estimates whether the model generalizes beyond the records used to construct it.

Decision trees encode classification as a sequence of attribute tests. Internal nodes test features, branches represent outcomes, and leaves provide class labels. ID3 recursively chooses the feature that best separates the training examples. Entropy measures remaining class uncertainty, and information gain measures the expected reduction in that uncertainty after a split. Choosing the largest gain tends to shorten classification paths, although it does not guarantee the smallest possible tree.

Trees can overfit noise or idiosyncrasies in a small sample. Prepruning stops growth when a proposed split offers too little gain; postpruning grows a larger tree and removes branches that fail validation or a complexity criterion. Bayesian classification provides a probabilistic alternative. A naive Bayes classifier combines class priors with attribute likelihoods under conditional independence, selecting the class with the largest posterior score. Its assumptions simplify computation and incremental learning, while its output preserves a probability-based basis for the prediction.

[[Association Rule Discovery]] searches for recurring co-occurrences rather than a single target class. A transaction database contains itemsets. Support counts how often an itemset appears, and a minimum-support threshold identifies frequent itemsets. Confidence measures how often the consequent appears among transactions containing the antecedent. These quantities describe empirical association, not causation.

The downward-closure property makes the combinatorial search practical: every subset of a frequent itemset must also be frequent, so an infrequent candidate eliminates all supersets containing it. Apriori repeatedly forms length-k candidates from the frequent sets of length k-1 and rescans the transactions for support. Frequent sets then generate implication rules that satisfy a confidence threshold. The same framework can represent binary, quantitative, or fuzzy relationships, provided support and membership are defined consistently.

### Establishing validity

[[Cluster Validity and Simulation]] asks whether a grouping is stable, fits the data, or recovers a known structure. External indices compare a captured clustering with an expected classification. Internal indices use only the observed data, proximity matrix, and clustering. Relative indices compare candidate clusterings or algorithms. Stability tests perturb the analysis by adding cases, removing features, changing initial conditions, or resampling and then examine whether the structure persists.

A cophenetic correlation compares the original proximity matrix with the cophenetic distances encoded by a dendrogram. Pair-counting indices compare whether pairs of observations are joined or separated in two partitions. The Rand index counts agreements, the adjusted or corrected Rand removes expected chance agreement, the Jaccard index focuses on shared positive assignments, and the Fowlkes-Mallows index balances common pair membership across solutions. Cohesion measures within-cluster nearness, separation measures distance from competing clusters, and the silhouette coefficient combines both for each observation.

When the theoretical baseline distribution of an index is unknown, Monte Carlo analysis builds one by repeatedly generating data under a stated random model, clustering it, computing the index, and comparing the observed value with the simulated distribution. The quality of that conclusion depends on the generator, seed discipline, model, and number of replications. Simulation can quantify how unusual a result is under assumptions; it cannot establish that those assumptions describe the application.

### Algorithms for categorical records

[[Categorical Data Clustering]] handles attributes whose values have no natural numeric order. ROCK defines neighbors through a categorical similarity threshold and defines a link between two records by their number of common neighbors. It agglomeratively merges the pair of clusters with the greatest positive goodness score until a requested number remains or usable links disappear.

STIRR represents each attribute value as a weighted node in a hypergraph. Iterative relational reinforcement propagates weights through tuples until the system reaches a fixed point, allowing strongly related values to emerge together. CACTUS identifies attribute values that co-occur more often than expected, stores inter-attribute and intra-attribute summaries, builds cluster projections, synthesizes candidate clusters, and validates them by support. CLICK constructs a multipartite graph from strongly connected attribute values, identifies maximal cliques, and merges supported candidates. Although their structures differ, all four methods replace geometric distance with evidence derived from categorical co-occurrence.

### Outliers and density

[[Outlier Detection and DBSCAN]] defines an outlier as an observation sufficiently unlike its context to suggest a different generating mechanism. A distance-based outlier has too few neighbors inside a specified radius. A local or density-based outlier can be near the data globally yet sparse relative to its immediate neighborhood. Local Outlier Factor compares neighborhood densities, while relative-density scores rank objects by how their density differs from that of nearby points.

Statistical rules use distributional distance. The empirical rule identifies extreme observations under approximate normality; distribution-free inequalities provide looser bounds. Mahalanobis distance accounts for covariance among dimensions, but ordinary estimates of the mean and covariance are themselves sensitive to outliers. The minimum covariance determinant estimates them from a compact subset to reduce that sensitivity. Clustering methods can also flag small, sparse groups, though the chosen cut, metric, and assumed number of clusters influence what is called anomalous.

DBSCAN grows clusters from dense neighborhoods using a radius and a minimum point count. Core points have enough neighbors, border points lie near a core without meeting the density threshold themselves, and noise points belong to neither category. Chains of density-reachable points form arbitrarily shaped clusters, and the algorithm does not require the number of clusters beforehand. Its global parameters can still fail when densities vary greatly or the proximity measure poorly represents the domain.

### Probabilistic and neural models

[[Model-Based Clustering]] treats observations as samples from a mixture of probability distributions. Each component represents a cluster with parameters such as a mean, covariance, and mixture weight. Gaussian mixtures produce ellipsoidal density contours and allow cluster overlap. The expectation-maximization algorithm estimates parameters by alternating probabilistic membership estimates with parameter updates, normally reaching a local likelihood maximum. Model selection then compares candidate numbers and covariance structures rather than choosing a cluster count independently of the probability model.

COBWEB offers an incremental conceptual alternative for nominal attributes. It stores a hierarchy of concepts, the probability of each concept, and conditional probabilities for attribute values. Category utility rewards partitions whose values are predictable within a class and predictive of class membership. For each new instance, COBWEB can incorporate it into a concept, create a new disjunct, merge concepts, or split an overly general one. CLASSIT extends the approach toward numeric attributes. These systems expose a central tradeoff: a richer probability representation supports inference and overlap, but costs more to store, update, and validate.

[[Neural Network Classification and Clustering]] supplies models whose decision boundaries are learned through weighted connections. A perceptron can separate linearly separable classes but cannot solve exclusive-or with one linear boundary. Multilayer networks introduce hidden units and nonlinear activation. Feedforward computation produces an output, and backpropagation uses gradient information to change weights in the direction that reduces error.

Competitive networks support unsupervised grouping by making output units compete to represent an input. A self-organizing map adds a neighborhood structure: the winning unit and nearby units update together, causing neighboring map locations to respond to neighboring regions of the input space. The result preserves aspects of topology and can support cluster visualization. As with other learned models, held-out data and interpretable diagnostics are needed because successful fitting does not by itself explain a decision.

### Data quality and interpretation

[[Cluster Data Quality and Interpretation]] returns the analysis to its inputs and purpose. Data cleansing investigates fields, removes or corrects errors, addresses missing values, and enforces domain and business rules. Accuracy, reliability, timeliness, relevance, and completeness describe complementary aspects of quality. Cleaning is ongoing because a once-valid dataset can become obsolete as codes, processes, and meanings change.

Attribute selection determines which distinctions the proximity calculation can see. Irrelevant dimensions can overwhelm useful structure, correlated categorical variables can count the same information repeatedly, and differences in scale can make one numerical feature dominate. Weighting and standardization are therefore modeling choices, not neutral housekeeping. The proximity measure must also fit the data type and the intended meaning of resemblance.

Interpretation finally asks what a cluster represents in the application. Domain experts may assess face validity, visualizations can expose shape and overlap, and quantitative indices can compare stability or fit. More than one clustering can legitimately represent the same data at different resolutions or under different purposes. Unequal density further complicates boundary decisions. The responsible conclusion describes the method, data preparation, parameters, alternatives, and uncertainties together with the groups it discovered.

Across the chapter, cluster analysis and data mining form a disciplined loop between representation and evidence. Proximity and attributes define what relationships are visible; algorithms compress those relationships into groups or rules; validation tests their stability and fit; and interpretation reconnects the mathematical result to the domain. The output becomes useful knowledge only when that whole chain remains explicit.

## Directly Referenced Tags

```query
path:"3 - Tags" "[[Cluster Analysis and Data Mining]]"
```
