import pandas as pd


def detect_outliers(df):
    results = []

    numeric_columns = df.select_dtypes(include="number").columns

    for column in numeric_columns:

        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)

        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df[
            (df[column] < lower_bound) |
            (df[column] > upper_bound)
        ][column]

        results.append({
            "Column": column,
            "Outliers": len(outliers),
            "Lower Bound": round(lower_bound, 2),
            "Upper Bound": round(upper_bound, 2)
        })

    return pd.DataFrame(results)