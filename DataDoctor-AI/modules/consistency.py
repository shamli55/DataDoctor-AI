import pandas as pd


def check_consistency(df):
    results = []

    # Check text/categorical columns
    categorical_columns = df.select_dtypes(
        include=["object", "string", "category"]
    ).columns

    for column in categorical_columns:

        values = df[column].dropna().astype(str)

        if values.empty:
            continue

        # Original unique values
        original_unique = values.nunique()

        # Normalize only for checking
        normalized = (
            values
            .str.strip()
            .str.lower()
            .str.replace(r"\s+", " ", regex=True)
        )

        normalized_unique = normalized.nunique()

        inconsistent = original_unique - normalized_unique

        results.append({
            "Column": column,
            "Original Unique": original_unique,
            "Normalized Unique": normalized_unique,
            "Possible Inconsistencies": max(int(inconsistent), 0)
        })

    # IMPORTANT:
    # Always return the expected columns,
    # even when there are no categorical columns.
    return pd.DataFrame(
        results,
        columns=[
            "Column",
            "Original Unique",
            "Normalized Unique",
            "Possible Inconsistencies"
        ]
    )