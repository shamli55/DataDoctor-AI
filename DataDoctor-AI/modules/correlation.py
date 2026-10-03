import pandas as pd


def correlation_analysis(df):

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.shape[1] < 2:
        return pd.DataFrame()

    return numeric_df.corr()