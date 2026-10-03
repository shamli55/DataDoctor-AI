import plotly.express as px


def missing_chart(df):

    missing = df.isnull().sum()

    missing = missing[
        missing > 0
    ].sort_values(ascending=False)

    if len(missing) == 0:
        return None

    fig = px.bar(
        x=missing.index,
        y=missing.values,
        labels={
            "x": "Column",
            "y": "Missing Values"
        },
        title="Missing Values by Column"
    )

    return fig


def correlation_heatmap(df):

    numeric_df = df.select_dtypes(
        include="number"
    )

    if numeric_df.shape[1] < 2:
        return None

    correlation = numeric_df.corr()

    fig = px.imshow(
        correlation,
        text_auto=True,
        title="Correlation Heatmap"
    )

    return fig