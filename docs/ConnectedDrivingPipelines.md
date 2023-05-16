# Connected Driving Pipelines

## Introduction

I created a few different connected driving pipelines. Each pipeline has improvements on the previous pipeline. Here are the current pipelines, ordered from latest to oldest:

## ConnectedDrivingPipelineV4 (4th Pipeline)

This is the latest connected driving pipeline. It has new features such as automatic caching, dependency injection, and context/path providers.

### Summary

This pipeline was created to end the continuous cycle of making maching learning (ML) pipelines for connected driving.

The pipeline was created for connected driving research. The goal is to create a better, more realistic dataset for training malicious bsm detection systems in the connected driving space. The current datasets, such as [Veremi](https://veremi-dataset.github.io/) and [Veremi Extension](https://github.com/josephkamel/VeReMi-Dataset) are too easy to train detection models for and don't model the world realistically.

We took the [Wyoming CV Pilot Basic Safety Message One Day Sample](https://www.opendatanetwork.com/dataset/data.transportation.gov/9k4m-a3jc) dataset from OpenDataNetwork as our original, real data.

This pipeline creates malicious datasets based on customizable attacks and then tests them using machine learning models such as [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), [Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) and [K-Nearest-Neighbours](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

You can visit the documentation at [www.aaroncollins.info/ConnectedDrivingPipelineV4/](https://www.aaroncollins.info/ConnectedDrivingPipelineV4/).

## Connecteddrivingresearch (3rd Pipeline)

### Summary

This pipeline was created to start generating BSMs rather than relying on the VEREMI dataset. It was messy and not very well documented. The 4th version was created to fix these issues.

This pipeline used real data from the [Wyoming CV Pilot Basic Safety Message One Day Sample](https://www.opendatanetwork.com/dataset/data.transportation.gov/9k4m-a3jc) dataset from OpenDataNetwork as our original, real data. We added malicious data to some of the BSMs and then trained machine learning models to detect the malicious BSMs.

You can see the repository at [github.com/aaron777collins/connecteddrivingresearch](https://github.com/aaron777collins/connecteddrivingresearch).

## ConnectedDrivingMachineLearningPipeline (2nd Pipeline)

### Summary

This pipeline used the [Veremi](https://veremi-dataset.github.io/) dataset to train machine learning models to detect malicious data within BSMs. It was a good start, but the dataset was too easy to train models for. Thus, the 3rd pipeline was created to generate more realistic data.

You can see the repository at [github.com/aaron777collins/ConnectedDrivingMachineLearningPipeline](https://github.com/aaron777collins/ConnectedDrivingMachineLearningPipeline).

## https://github.com/aaron777collins/ConnectedDrivingDataGenerator (1st Pipeline)

### Summary

This pipeline was actually built off of [VEINS](https://veins.car2x.org/tutorial/) to simulate cars talking to eachother in a virtual environment. Most of the code was taken from the VEINS tutorial and modified to fit our needs. This pipeline was abandoned because of the difficulty setting it up and making changes to fix our needs. The high learning curve was not worth it when we could just use the [Veremi](https://veremi-dataset.github.io/) dataset. No machine learning was done in this pipeline.

You can see the repository at [github.com/aaron777collins/ConnectedDrivingDataGenerator](https://github.com/aaron777collins/ConnectedDrivingDataGenerator).

## Links
- [ConnectedDrivingPipelineV4 Docs](https://www.aaroncollins.info/ConnectedDrivingPipelineV4/)
- [ConnectedDrivingPipelineV4 Github Repo](https://github.com/aaron777collins/ConnectedDrivingPipelineV4)
- [connecteddrivingresearch Github Repo](https://github.com/aaron777collins/connecteddrivingresearch)
- [ConnectedDrivingMachineLearningPipeline Github Repo](https://github.com/aaron777collins/ConnectedDrivingMachineLearningPipeline)
- [ConnectedDrivingDataGenerator Github Repo](https://github.com/aaron777collins/ConnectedDrivingDataGenerator)
- [VEINS](https://veins.car2x.org/tutorial/)
- [Veremi](https://veremi-dataset.github.io/)
- [Veremi Extension](https://github.com/josephkamel/VeReMi-Dataset)
- [Wyoming CV Pilot Basic Safety Message One Day Sample](https://www.opendatanetwork.com/dataset/data.transportation.gov/9k4m-a3jc)
- [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
- [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
- [K-Nearest-Neighbours Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
