import pandas as pd


def get_basic_profile(df):
    profile = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_cells": int(df.isnull().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
        "numeric_columns": len(df.select_dtypes(include="number").columns),
        "categorical_columns": len(df.select_dtypes(include="object").columns)
    }

    return profile


def get_column_profile(df):
    result = []

    for column in df.columns:
        result.append({
            "Column": column,
            "Data Type": str(df[column].dtype),
            "Missing": int(df[column].isnull().sum()),
            "Missing %": round(df[column].isnull().mean() * 100, 2),
            "Unique Values": int(df[column].nunique()),
            "Unique %": round(df[column].nunique() / len(df) * 100, 2)
        })

    return pd.DataFrame(result)