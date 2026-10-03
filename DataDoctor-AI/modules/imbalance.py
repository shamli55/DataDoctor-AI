def analyze_imbalance(df, target):

    if target not in df.columns:
        return None

    counts = df[target].value_counts()

    percentages = df[target].value_counts(
        normalize=True
    ) * 100

    result = []

    for category in counts.index:

        result.append({
            "Class": category,
            "Count": int(counts[category]),
            "Percentage": round(percentages[category], 2)
        })

    return result