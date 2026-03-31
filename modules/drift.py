from scipy.stats import ks_2samp

def detect_drift(df1, df2):
    drift_result = {}

    for col in df1.select_dtypes(include=['int64','float64']).columns:
        stat, p_value = ks_2samp(df1[col], df2[col])
        drift_result[col] = p_value

    return drift_result