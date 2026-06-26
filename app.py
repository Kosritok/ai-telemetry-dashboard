import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Edge AI Telemetry Console", layout="wide")

st.markdown("""
    <style>
    .reportview-container { background: #f0f2f6; }
    .stMetric { background-color: #8A2BE2; padding: 15px; border-radius: 10px; box-shadow: 2px 2px 5px rgba(0,0,255,0.05);}
    </style>
    """, unsafe_allow_html=True)

@st.cache_data
def load_and_normalize_data():
    try:
        df = pd.read_csv('edge_model_logs.csv')
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        return df
    except FileNotFoundError:
        st.error("Please run first the file 'generate_mock_data.py' to create the logs")
        return pd.DataFrame()
    
df_logs = load_and_normalize_data()

if not df_logs.empty:
    st.sidebar.title("Console Controls & Alerts")

    confidence_threshold = st.sidebar.slider(
        "Model Confidence Treshold (%)",
        min_value = 65.0, max_value=95.0, value=80.0, step=1.0
    )

    latest_data = df_logs.iloc[-1]
    current_confidence = latest_data['confidence_score']

    st.sidebar.markdown("---")
    st.sidebar.subheader("Live Alert Feed")

    if current_confidence < confidence_threshold:
        st.sidebar.error(f"CRITICAL ALERT: Model Confidence Dropped to {current_confidence:.2%}")
        st.sidebar.markdown("""
            **Explainable AI (XAI) Root-Cause Analysis:**
            *   **Issue:** Heavy frame occlusion or sudden low-lighting detected.
            *   **Hardware State:** Thermal throttling observed; latency increased.
            *   **Action:** System fallback activated. Evaluator review suggested.
        """)
    else:
        st.sidebar.success("System Status: Nominal. Model performance within stable thresholds.")

    st.title("Edge Telemetry & Performance Dashboard")
    st.markdown("Evaluation Console for Real-Time Model Deployments.")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Inference Latency", value=f"{latest_data['latency_ms']:.2f} ms", delta="-1.2ms")
    with col2:
        st.metric(label="Frame Rate", value=f"{latest_data['fps']:.1f} FPS", delta="0.4 FPS")
    with col3:
        st.metric(label="Model Confidence", value=f"{current_confidence:.1f}%", delta=f"{(current_confidence - confidence_threshold):.1f}% vs Threshold")
    
    st.markdown("---")

    #Interactive Charts Zone
    st.subheader("Historical Performance Over Time")

    #Graphic
    fig_confidence = px.line(
        df_logs.tail(100), x='timestamp', y='confidence_score',
        title="Model Confidence Score (Last 100 entries)",
        labels={'confidence_score': 'Confidence (%)', 'timestamp': 'Time'}
    )
    fig_confidence.add_hline(y=confidence_threshold, line_dash="dash", line_color="red", annotation_text="Threshold")
    fig_confidence.update_layout(template="plotly_white")
    st.plotly_chart(fig_confidence, use_container_width=True)