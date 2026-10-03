import pandas as pd
import numpy as np


def detect_leakage(df, target):

    # Check target exists
    if target not in df.columns:
        return pd.DataFrame()

    results = []

    # Encode target
    target_data = df[target].copy()

    if target_data.dtype == "object":
        target_encoded = pd.factorize(
            target_data.fillna("Missing").astype(str)
        )[0]
    else:
        target_encoded = pd.to_numeric(
            target_data,
            errors="coerce"
        )

    for column in df.columns:

        # Skip target column
        if column == target:
            continue

        feature = df[column].copy()

        # Convert feature into numeric values
        if feature.dtype == "object":
            feature_encoded = pd.factorize(
                feature.fillna("Missing").astype(str)
            )[0]
        else:
            feature_encoded = pd.to_numeric(
                feature,
                errors="coerce"
            )

        # Create temporary dataframe
        temp = pd.DataFrame({
            "feature": feature_encoded,
            "target": target_encoded
        })

        # Remove invalid values
        temp = temp.replace(
            [np.inf, -np.inf],
            np.nan
        ).dropna()

        # Need at least 2 rows
        if len(temp) < 2:
            correlation = 0
        else:
            correlation = temp["feature"].corr(
                temp["target"]
            )

            if pd.isna(correlation):
                correlation = 0

        absolute_correlation = abs(correlation)

        # Leakage risk
        if absolute_correlation >= 0.90:
            risk = "🔴 High"
        elif absolute_correlation >= 0.60:
            risk = "🟡 Medium"
        else:
            risk = "🟢 Low"

        results.append({
            "Feature": column,
            "Correlation": round(correlation, 3),
            "Absolute Correlation": round(
                absolute_correlation, 3
            ),
            "Leakage Risk": risk
        })

    return pd.DataFrame(results)