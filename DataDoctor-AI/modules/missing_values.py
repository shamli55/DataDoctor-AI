def analyze_missing_values(df):
    result = []

    for column in df.columns:
        missing = df[column].isnull().sum()
        percentage = (missing / len(df)) * 100

        result.append({
            "Column": column,
            "Missing Count": int(missing),
            "Missing %": round(percentage, 2)
        })

    return result