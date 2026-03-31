import streamlit as st
import pandas as pd
import tempfile
from modules.profiling import analyze_data
from modules.etl_recommend import recommend_etl
from modules.pyspark_etl import run_etl
from modules.drift import detect_drift

st.title("AI-Powered Data Understanding & ETL System")

# Upload original dataset
file = st.file_uploader("Upload Original CSV File", type=["csv"])

if file:
    df = pd.read_csv(file)

    # Preview
    st.subheader("Dataset Preview")
    st.write(df.head())

    # Analysis
    st.subheader("Dataset Analysis")
    summary = analyze_data(df)
    st.write(summary)

    # ETL Recommendation
    st.subheader("ETL Recommendations")
    recs = recommend_etl(df)
    st.write(recs)

    # ETL Execution
    if st.button("Run ETL (PySpark)"):
        st.info("Running ETL...")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            tmp.write(file.getbuffer())
            temp_path = tmp.name

        cleaned_df = run_etl(temp_path)

        st.success("ETL Completed Successfully!")

    # ==============================
    # DRIFT DETECTION
    # ==============================

    st.subheader("Data Drift Detection")

    file2 = st.file_uploader("Upload New Dataset for Drift Detection", type=["csv"], key="new")

    if file2:
        df2 = pd.read_csv(file2)

        st.write("New Dataset Preview")
        st.write(df2.head())

        st.subheader("Drift Detection Results")

        drift = detect_drift(df, df2)

        for col, p in drift.items():
            if p < 0.05:
                st.error(f"{col}: Drift Detected ❌ (p-value={p:.4f})")
            else:
                st.success(f"{col}: No Drift ✅ (p-value={p:.4f})")