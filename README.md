# Evolutionary Data Measures: Understanding the Difficulty of Text Classification Tasks : Datasets Code

**Authors:** _Ed Collins, Nikolai Rozanov, Bingbing Zhang_

**Contact:** _contact@wluper.com_

In the paper "Evolutionary Data Measures: Understanding the Difficulty of Text Classification Tasks" we develop a 
measure of the difficulty of text classification tasks by training 12 different machine learning models on 78 different 
text classification datasets. We proceed to demonstrate that our measure generalises to eight datasets from [1], only one of which we use during training, and 
perform an error analysis with 4 fake, synthetically generated datasets.

We have made all 89 of the datasets which we made use of during the course of the research, all in the same format with references, available from <http://data.wluper.com>. In this repo, we provide code to load any of the downloaded datasets and demonstrate how to use our difficulty-calculating code to analyse the difficulty of a dataset.

Each dataset that can be downloaded from <http://data.wluper.com> has a top level directory corresponding to its name, and two subdirectories: "training/" and "eval/". 
"training/" contains a single .csv file for the training data of each dataset. "eval/" contains a single .csv file for 
the test set and optionally another .csv file for the validation set.

The structure of the dataset directories is:

```
DATASET_NAME/
        |
        |_ README.md
        |
        |_ eval/
        |      |
        |      |_ DATASET_NAME__TEST.csv
        |      |
        |      |_ DATASET_NAME__DEV.csv (optional)
        |
        |_ training/
               |
               |_ DATASET_NAME__FULL.csv
```

Each .csv file contains two columns. The first item in the column is the item of text and the second item is the label 
for that text.

We also provide the file _"difficulties.csv"_ which contains the statistics from our difficulty measure presented in the
 paper for every dataset.

Finally, we provide code files:

1. `data_loader.py` - this contains two functions, one for loading individual .csv files with precisely two columns 
(as our data is setup) and one for loading an entire dataset from a directory into a dictionary, with keys "TRAIN", 
"VALID" and "TEST" and values as a tuple of lists - one list for text and one for labels.

2. `calculate_all_difficulties.py` - this code will calculate our difficulty measure for every provided dataset and put 
the results in "all_difficulties.csv" (this will be identical to the provided "difficulties.csv" but is provided for 
demonstration purposes). Note that the code package for calculating difficulty measures (provided separately) must be 
pip-installed locally for this code file to run.

3. `demo.py` - this code demonstrates how to use the provided data loading code and to run our difficulty calculating 
code on the loaded dataset. It requires that the difficulty calculating code package be pip-installed locally.


#### References

[1] Zhang, X., Zhao, J. and LeCun, Y., 2015. Character-level convolutional networks for text classification. In Advances
    in neural information processing systems (pp. 649-657).