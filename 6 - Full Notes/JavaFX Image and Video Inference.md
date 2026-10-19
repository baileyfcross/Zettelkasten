2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Web Cloud and Data Applications]]

# JavaFX Image and Video Inference

Visual JavaFX content can become neural-network input by taking a snapshot and converting its pixels into the numeric representation expected by a model. The book applies this pattern to drawings based on animal classes from the Quick, Draw! data set. Images are normalized to small black-and-white inputs, and a LeNet-style convolutional network predicts the depicted class.

The same bridge supports video object detection. Frames are passed to pretrained TinyYOLO or YOLO2 models, which predict class probabilities and bounding boxes that JavaFX can overlay on the running image. In both cases, capture and display belong to the UI while tensor conversion and inference use the pipeline in [[JavaFX Machine Learning with DeepLearning4J]]. Thread separation keeps the live interface responsive.

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
