# Breast-Cancer-Diagnosis
Breast-Cancer-Diagnosis

**Table of content**

- [Project Overview](#overview)
- [Requirements](#requirements)
- [Installation](#installation)
- [Data](#data)
- [Scripts](#pacakage_scripts)



## Overview



## Requirements
The project requires Python 3.6+, and python packages listed in `requirements.txt` file

## Installation 

1. Creating conda virtual environment [in Linux]
```
conda create -n env
conda activate env
conda config  --env --add channels conda-forge
conda config --env --set channel_priority strict
```

2. Cloning the repo and install the dependency packages using `requirements.txt`
```
git clone https://github.com/Caphace-Ethan/Breast-Cancer-Diagnosis
cd Breast-Cancer-Diagnosis
conda install -r requirements.txt or try using pip instead of conda

sudo apt-get install graphviz or conda install python-graphviz
```

## Data

### The Dataset Contains the following Attributes

* radius (mean of distances from center to points on the perimeter)
* texture (standard deviation of gray-scale values)
* perimeter
* area
* smoothness (local variation in radius lengths)
* compactness (perimeter^2 / area - 1.0)
* concavity (severity of concave portions of the contour)
* concave points (number of concave portions of the contour)
* symmetry
* fractal dimension ("coastline approximation" - 1)

The mean, standard error (SE) and "worst" or largest (mean of the three largest values) of these features were computed for each image


## Package_Scripts
Package Scripts are found in ```scripts``` directory, its content is explained below.

- ```FileHandler:``` Helper class for reading and writing different file formats.
- ```package_config: ```Script for handling package configurations such as location of files and url(s), etc.
- ```data_processor: ```Script for performing data processing for example computing missing values, fixing outliers, etc.
- ```plot: ```Script for ploting different figures including box-plot, scatter-plot, histogram, bar-plot, etc.
- ```log: ```script for logging package logs
