import pandas as pd


def clean_data(df):

    cleaned = df.copy()

    # Remove duplicate rows
    cleaned = cleaned.drop_duplicates()

    # Standardize text columns
    text_columns = cleaned.select_dtypes(
        include=["object"]
    ).columns

    for column in text_columns:

        cleaned[column] = (
            cleaned[column]
            .astype("string")
            .str.strip()
        )

    # Fill numeric missing values
    numeric_columns = cleaned.select_dtypes(
        include="number"
    ).columns

    for column in numeric_columns:

        cleaned[column] = cleaned[column].fillna(
            cleaned[column].median()
        )

    # Fill categorical missing values
    for column in text_columns:

        mode = cleaned[column].mode()

        if not mode.empty:
            cleaned[column] = cleaned[column].fillna(
                mode.iloc[0]
            )

    return cleaned