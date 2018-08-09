"""
demo.py: provides a demonstration of using our difficulty calculating code.

NOTE: for this to run, the difficulty calculating package must be installed locally. It also assumes that the dataset
      to calculate the difficulty for is in the same directory as this code file and that you are running the code from
      that same directory.
"""

# ======================================================================================================================
#
# CODE SETUP
#
# ======================================================================================================================

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
# MAIN
#
# ======================================================================================================================

datasetName       = "SST_2"

dataset           = data_loader.load_dataset(datasetName)

trSents, trLabels = dataset["TRAIN"]

difficultyReport  = report.get_difficulty_report(sents=trSents, labels=trLabels)

print(difficultyReport)


# ======================================================================================================================
