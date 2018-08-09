"""
calculate_results.py: applies the difficulty calculating code to every dataset in the current working directory.

In the paper corresponding to this code, we present a measure of difficulty for text classification datasets. In the
directory alongside this code are 90 different datasets which we made use of in varying capacity in the paper. This code
applies the difficulty calculating code to every dataset in the current working directory and writes the results to
"all_difficulties.csv" in the current working directory.

This code requires that the "edm" package be installed to run.
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

# ====>> Own Package Imports <<====
from edm import report
import data_loader

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

def iterate_datasets(startDir):
    """
    Iterates over all datasets. Each directory must have the same directory structure for this function:

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

    :param startDir : the directory to iterate over datasets from.
    :type startDir  : str

    :returns        : the training dataset path, the name of the dataset directory.
    """
    for dirname in os.listdir(startDir):
        dirpath = startDir + "/" + dirname

        if not os.path.isdir(dirpath) or dirname.startswith(".") or dirname.startswith("__"):
            continue

        dsetPath = dirpath + "/training/" + dirname + "__FULL.csv"

        yield dsetPath, dirname

# ======================================================================================================================


if __name__ == '__main__':

    for dsetPath, dsetName in iterate_datasets(os.getcwd()):

        print("----> Loading {} data...".format(dsetName), end=" ")
        sys.stdout.flush()

        sents, labels = data_loader.load_two_column_csv_data(dsetPath)

        print("Done.")

        difficultyResults = report.get_difficulty_components_dict(sents, labels)

        result = (
            dsetName,
            difficultyResults["Distinct Words : Total Words"][0] ,
            difficultyResults["Class Imbalance"][0]              ,
            difficultyResults["Class Diversity"][0]              ,
            1 - difficultyResults["1 - Min. Hell. Dist."][0]     ,
            difficultyResults["Mutual Information"][0]           ,
            difficultyResults["Difficulty"][0]
        )

        with open("all_difficulties.csv", "a") as f:

            writer = csv.writer(f)
            writer.writerow(result)

