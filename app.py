import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

from src.genai_analyzer import generate_threat_analysis

# ============================================================
# CONFIGURATION
# ============================================================

MODEL_PATH = r"models\cyber_threat_model.pkl"
ENCODER_PATH = r"models\label_encoder.pkl"

st.set_page_config(
    page_title="AI Cyber Threat Detection",
    page_icon="🛡️",
    layout="wide"
)

# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)
    return model, encoder


# ============================================================
# HEADER
# ============================================================

st.title("🛡️ AI Cyber Threat Detection System")

st.write(
    "Upload network-flow data and use the trained "
    "Random Forest model to detect potential cyber threats."
)

# ============================================================
# CHECK MODEL
# ============================================================

if not os.path.exists(MODEL_PATH):
    st.error(f"Model not found: {MODEL_PATH}")
    st.stop()

if not os.path.exists(ENCODER_PATH):
    st.error(f"Label encoder not found: {ENCODER_PATH}")
    st.stop()

model, label_encoder = load_model()

# ============================================================
# SYSTEM INFORMATION
# ============================================================

st.sidebar.header("System Information")

st.sidebar.success("Model Loaded")

st.sidebar.write(
    f"**Model:** {type(model).__name__}"
)

st.sidebar.write(
    f"**Features:** {model.n_features_in_}"
)

st.sidebar.write(
    f"**Classes:** {len(label_encoder.classes_)}"
)

# ============================================================
# FILE UPLOAD
# ============================================================

uploaded_file = st.file_uploader(
    "Upload Network Flow CSV",
    type=["csv"]
)

if uploaded_file is None:
    st.info("👆 Upload a network-flow CSV file to begin detection.")
    st.stop()

# ============================================================
# READ DATA
# ============================================================

try:

    df = pd.read_csv(uploaded_file)

except Exception as e:

    st.error(f"Could not read CSV file: {e}")
    st.stop()

st.subheader("📄 Uploaded Dataset")

col1, col2 = st.columns(2)

with col1:
    st.metric("Rows", f"{len(df):,}")

with col2:
    st.metric("Columns", len(df.columns))

# ============================================================
# PREPARE FEATURES
# ============================================================

# Save the actual labels if the uploaded dataset contains them
actual_labels = None

# Remove accidental spaces from column names
df.columns = df.columns.str.strip()

if "Label" in df.columns:
    actual_labels = df["Label"].copy()
    X = df.drop(columns=["Label"]).copy()
else:
    X = df.copy()

st.write(f"Features after removing Label: {X.shape[1]}")
# ============================================================
# HANDLE DATA TYPES
# ============================================================

X = X.replace([np.inf, -np.inf], np.nan)

X = X.apply(
    pd.to_numeric,
    errors="coerce"
)

X = X.fillna(0)

# ============================================================
# CHECK FEATURE COUNT
# ============================================================

expected_features = model.n_features_in_

if X.shape[1] != expected_features:

    st.error(
        f"Invalid number of features. "
        f"Model expects {expected_features} features "
        f"but received {X.shape[1]}."
    )

    st.write("Features detected:")
    st.write(list(X.columns))

    st.stop()

# ============================================================
# PREDICTION
# ============================================================

if st.button("🔍 Detect Threats", type="primary"):

    with st.spinner("AI model is analyzing the network traffic..."):

        predictions = model.predict(X)

        predicted_labels = label_encoder.inverse_transform(
            predictions
        )

    # ========================================================
    # RESULTS
    # ========================================================

    st.session_state["detection_complete"] = True
    st.success("Threat detection completed!")

    result_df = df.copy()

    result_df["Predicted Threat"] = predicted_labels

    # ========================================================
    # SUMMARY
    # ========================================================

    st.subheader("📊 Detection Summary")

    counts = pd.Series(predicted_labels).value_counts()

    total = len(predicted_labels)

    benign_count = counts.get("BENIGN", 0)

    threat_count = total - benign_count

    # Save results for Generative AI analysis
    st.session_state["predicted_labels"] = predicted_labels
    st.session_state["total"] = total
    st.session_state["benign_count"] = benign_count
    st.session_state["threat_count"] = threat_count

    try:
        probabilities = model.predict_proba(X)

        confidence = float(
            np.max(probabilities, axis=1).mean() * 100
        )

    except Exception:
        confidence = 0.0

    st.session_state["confidence"] = confidence

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Total Flows",
            f"{total:,}"
        )

    with c2:
        st.metric(
            "Benign",
            f"{benign_count:,}"
        )

    with c3:
        st.metric(
            "Threats",
            f"{threat_count:,}"
        )

    # ========================================================
    # THREAT DISTRIBUTION
    # ========================================================

    st.subheader("🚨 Threat Distribution")

    distribution = (
        pd.Series(predicted_labels)
        .value_counts()
        .rename_axis("Threat")
        .reset_index(name="Count")
    )

    st.dataframe(
        distribution,
        use_container_width=True
    )

    # ========================================================
    # CHART
    # ========================================================

    st.bar_chart(
        distribution.set_index("Threat")
    )


    # ========================================================
    # PREDICTION RESULTS
    # ========================================================

    st.subheader("🔎 Prediction Results")

    st.dataframe(
        result_df.head(1000),
        use_container_width=True
    )

    if len(result_df) > 1000:
        st.info(
            "Showing first 1,000 rows for performance. "
            f"Total predictions: {len(result_df):,}"
        )

    # ========================================================
    # DOWNLOAD RESULTS
    # ========================================================

    csv_data = result_df.to_csv(index=False)

    st.download_button(
        label="⬇️ Download Detection Results",
        data=csv_data,
        file_name="threat_detection_results.csv",
        mime="text/csv"
    )

    # ========================================================
    # ACTUAL VS PREDICTED
    # ========================================================

    if actual_labels is not None:

        st.subheader("🎯 Actual vs Predicted")

        comparison = pd.DataFrame({
            "Actual": actual_labels,
            "Predicted": predicted_labels
        })
        st.dataframe(
            comparison.head(1000),
            use_container_width=True
        )

# ============================================================
# GENERATIVE AI ANALYSIS
# ============================================================

if st.session_state.get("detection_complete", False):

    st.divider()

    st.subheader("🤖 Generative AI Threat Analysis")

    st.write(
        "Use Generative AI to explain the machine-learning "
        "detection results and provide defensive recommendations."
    )

    if st.button("🤖 Generate AI Security Analysis"):

        # Retrieve saved detection results
        saved_labels = st.session_state["predicted_labels"]
        saved_total = st.session_state["total"]
        saved_benign = st.session_state["benign_count"]
        saved_threat = st.session_state["threat_count"]

        saved_counts = pd.Series(saved_labels).value_counts()

        saved_top_threats = saved_counts.to_dict()

        saved_primary_threat = (
            saved_counts
            .drop(labels=["BENIGN"], errors="ignore")
            .idxmax()
            if saved_threat > 0
            else "BENIGN"
        )

        saved_confidence = st.session_state.get(
            "confidence",
            0.0
        )

        with st.spinner(
            "Generative AI is analyzing the detection results..."
        ):

            ai_analysis = generate_threat_analysis(
                prediction=str(saved_primary_threat),
                confidence=saved_confidence,
                total_flows=saved_total,
                threat_flows=saved_threat,
                benign_flows=saved_benign,
                top_threats=saved_top_threats
            )

        st.markdown(ai_analysis)

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "AI Cyber Threat Detection | Random Forest + Generative AI"
)
