def calculate_health_score(
    df,
    missing_count,
    duplicate_count,
    outlier_count,
    consistency_issues
):

    total_cells = df.shape[0] * df.shape[1]

    missing_penalty = (
        (missing_count / total_cells) * 30
        if total_cells > 0 else 0
    )

    duplicate_penalty = (
        (duplicate_count / len(df)) * 20
        if len(df) > 0 else 0
    )

    outlier_penalty = (
        (outlier_count / total_cells) * 20
        if total_cells > 0 else 0
    )

    consistency_penalty = min(
        consistency_issues * 2,
        20
    )

    score = 100 - (
        missing_penalty
        + duplicate_penalty
        + outlier_penalty
        + consistency_penalty
    )

    return round(max(0, min(score, 100)), 2)


def health_status(score):

    if score >= 80:
        return "Healthy"

    elif score >= 60:
        return "Needs Attention"

    else:
        return "Poor Quality"