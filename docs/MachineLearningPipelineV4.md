## Summary

This pipeline was created to end the continuous cycle of making maching learning (ML) pipelines.

This version of the pipeline was created for connected driving research. The goal is to create a better, more realistic dataset for training malicious bsm detection systems in the connected driving space. The current datasets, such as [Veremi](https://veremi-dataset.github.io/) and [Veremi Extension](https://github.com/josephkamel/VeReMi-Dataset) are too easy to train detection models for and don't model the world realistically.

We took the [Wyoming CV Pilot Basic Safety Message One Day Sample](https://www.opendatanetwork.com/dataset/data.transportation.gov/9k4m-a3jc) dataset from OpenDataNetwork as our original, real data.

This pipeline creates malicious datasets based on customizable attacks and then tests them using machine learning models such as [Random Forest](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html), [Decision Tree](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) and [K-Nearest-Neighbours](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).

You can visit the documentation at [www.aaroncollins.info/MachineLearningPipelineV4/](https://www.aaroncollins.info/MachineLearningPipelineV4/).

## Links
- [MachineLearningPipelineV4 Docs](https://www.aaroncollins.info/MachineLearningPipelineV4/)
- [Github Repo](https://github.com/aaron777collins/MachineLearningPipelineV4)
