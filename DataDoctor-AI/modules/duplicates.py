def analyze_duplicates(df):
    duplicate_count = int(df.duplicated().sum())

    return {
        "duplicate_count": duplicate_count,
        "duplicate_percentage": round(
            duplicate_count / len(df) * 100, 2
        )
    }