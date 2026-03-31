def recommend_etl(df):
    recommendations = []

    if df.isnull().sum().sum() > 0:
        recommendations.append("Fill missing values")

    if df.duplicated().sum() > 0:
        recommendations.append("Remove duplicate rows")

    if len(df.select_dtypes(include='object').columns) > 0:
        recommendations.append("Encode categorical columns")

    return recommendations