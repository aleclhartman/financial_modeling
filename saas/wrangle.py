# import data science libraries
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

def acquire_saas_data():
    """
    This function returns a DataFrame with the data from the saas.csv file.
    """

    df = pd.read_csv("saas.csv")
    
    return df

def prepare_saas_data(df):
    """
    This function returns the saas DataFrame with all necessary preparation conducted for EDA and forecasting.
    """

    # rename features
    df.rename(
        columns={
            "Month_Invoiced": "invoice_month",
            "Customer_Id": "customer_id",
            "Invoice_Id": "invoice_id",
            "Subscription_Type": "subscription_type",
            "Amount": "amount",
        },
        inplace=True,
    )

    # transform invoice_month from object dtype to datetime dtype
    df["invoice_month"] = pd.to_datetime(df["invoice_month"])

    # use invoice_month as index
    df = df.sort_values("invoice_month").set_index("invoice_month")

    return df

def wrangle_saas_data():
    """
    This function wrangles the saas data and returns it as the df variable.
    """

    # acquire
    df = acquire_saas_data()

    # prepare
    df = prepare_saas_data(df)

    return df