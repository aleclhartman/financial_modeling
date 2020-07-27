# import data science libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

import wrangle as wr

def split_saas_data(df):
    """
    This function splits the saas data into train and test for EDA and forecasting.
    """

    train = df.loc[:"2016-12-31"]
    test = df.loc["2017-01-31":]

    return train, test