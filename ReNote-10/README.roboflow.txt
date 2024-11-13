
ReNote - v10 2024-11-13 10-23am
==============================

This dataset was exported via roboflow.com on November 13, 2024 at 10:27 AM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 420 images.
Receipt-label are annotated in YOLOv8 format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 1280x1280 (Stretch)

The following augmentation was applied to create 5 versions of each source image:
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise, upside-down
* Random Gaussian blur of between 0 and 1.5 pixels
* Salt and pepper noise was applied to 1 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Random brigthness adjustment of between -10 and +10 percent


