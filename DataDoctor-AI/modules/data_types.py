def analyze_data_types(df):

    result = []

    for column in df.columns:

        dtype = str(df[column].dtype)

        if dtype == "object":
            detected_type = "Categorical/Text"
        elif "int" in dtype:
            detected_type = "Integer"
        elif "float" in dtype:
            detected_type = "Numeric"
        elif "datetime" in dtype:
            detected_type = "Date/Time"
        else:
            detected_type = dtype

        result.append({
            "Column": column,
            "Pandas Type": dtype,
            "Detected Type": detected_type
        })

    return result