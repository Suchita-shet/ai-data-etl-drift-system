def analyze_data(df):
    summary = {
        "Total Rows": df.shape[0],
        "Total Columns": df.shape[1],
        "Missing Values": df.isnull().sum().to_dict(),
        "Duplicate Rows": int(df.duplicated().sum())
    }
    return summary