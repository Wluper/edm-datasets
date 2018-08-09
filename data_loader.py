"""
data_loader.py: provides functions to load the provided data into memory.

This code can load datasets with the following package structure:

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

All provided datasets already have this format.
"""

# ======================================================================================================================
#
# CODE SETUP
#
# ======================================================================================================================

# ====>> Python Native Imports <<====
import os
import sys
import csv
csv.field_size_limit(sys.maxsize)  # For the Sougou dataset

# ====>> Authorship Info <<====
__author__  = ["Ed Collins", "Nikolai Rozanov", "Bingbing Zhang"]
__licence__ = "MIT"
__version__ = "0.0.1"

# ======================================================================================================================


# ======================================================================================================================
#
# FUNCTIONS
#
# ======================================================================================================================


def load_two_column_csv_data(fullPath):
    """
    Loads data from a .csv file with precisely two columns and returns them as two lists.

    :param fullPath : the full path to the .csv file to load.
    :type fullPath  : str

    :return         : list of column 1 from the .csv file, list of column 2 from the .csv file
    """
    listOne, listTwo = [], []

    with open(fullPath, "r") as f:

        reader = csv.reader(f)

        for line in reader:

            if not line:
                continue

            assert len(line) == 2, "This function is only for two column .csv data."

            listOne.append(line[0])
            listTwo.append(line[1])

    return listOne, listTwo


def _load_all(trainPath, validPath, testPath):
    """
    Performs the actual loading of the datasets.

    :param trainPath  : path to training data.
    :type trainPath   : str

    :param validPath  : path to the validation data, may not exist as there is not always a validation set.
    :type validPath   : str

    :param testPath   : path to testing data.
    :type testPath    : str

    :return           : dictionary mapping train, valid and test to tuples of the data: (text, label)
    """

    if os.path.exists(validPath):

        return {"TRAIN" : load_two_column_csv_data(trainPath),
                "VALID" : load_two_column_csv_data(validPath),
                "TEST"  : load_two_column_csv_data(testPath)}

    else:

        return {"TRAIN" : load_two_column_csv_data(trainPath),
                "TEST"  : load_two_column_csv_data(testPath)}


def load_dataset(datasetName):
    """
    Loads a dataset into a dictionary. Note that the dataset directory must have the following format:

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

    It also assumes that this directory will be stored in the CURRENT WORKING DIRECTORY.

    :param datasetName : the name of the dataset to load (which is the same name as the top level directory.
    :type datasetName  : str

    :return            : a dictionary containing train, valid (optional) and test sets. Keys are the set name, values
                         a tuple of lists, the first one being sentences and the second labels.
    """
    if datasetName.endswith("/"):
        datasetName = datasetName.strip("/")

    trainPath = datasetName + "/training/" + datasetName + "__FULL.csv"
    validPath = datasetName + "/eval/"     + datasetName + "__DEV.csv"
    testPath  = datasetName + "/eval/"     + datasetName + "__TEST.csv"

    return _load_all(trainPath, validPath, testPath)

# ======================================================================================================================
