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
conda install -r requirements.txt
```

## Data

- The 

## Package_Scripts
Package Scripts are found in ```scripts``` directory, its content is explained below.

- ```FileHandler:``` Helper class for reading and writing different file formats.
- ```package_config: ```Script for handling package configurations such as location of files and url(s), etc.
- ```log: ```script for logging package logs
