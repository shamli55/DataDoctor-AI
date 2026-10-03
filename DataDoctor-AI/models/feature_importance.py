import pandas as pd

from sklearn.ensemble import RandomForestClassifier


def calculate_feature_importance(df, target):

    if target not in df.columns:
        return pd.DataFrame()

    data = df.copy()

    X = data.drop(columns=[target])
    y = data[target]

    # Convert categorical columns
    X = pd.get_dummies(
        X,
        drop_first=True
    )

    # Fill missing values
    X = X.fillna(0)

    # Target must be converted to numeric
    y = y.astype("category").cat.codes

    if y.nunique() < 2:
        return pd.DataFrame()

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    })

    return importance.sort_values(
        "Importance",
        ascending=False
    ).head(15)