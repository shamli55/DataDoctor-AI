import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def detect_anomalies(df):

    numeric_df = df.select_dtypes(
        include="number"
    ).copy()

    if numeric_df.shape[1] < 1:
        return df.copy(), 0

    numeric_df = numeric_df.fillna(
        numeric_df.median()
    )

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(numeric_df)

    model = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    predictions = model.fit_predict(
        scaled_data
    )

    result = df.copy()

    result["Anomaly"] = predictions

    anomaly_count = int(
        (predictions == -1).sum()
    )

    return result, anomaly_count