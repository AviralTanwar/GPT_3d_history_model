import streamlit as st
import plotly.graph_objects as go
from graph_builder import build_topic_graph

st.set_page_config(page_title="Topic Graph", layout="wide")

st.markdown(
    """
    <style>
        body { background-color: #0a0f1a !important; color: #e2e8f0; }
        .stApp { background-color: #0a0f1a !important; }
        .css-18ni7ap, .css-1d391kg { background-color: #0a0f1a !important; }
    </style>
    """, unsafe_allow_html=True
)

st.title("🪐 Topic Graph — See Your Mind in Motion")

if "conversations" not in st.session_state:
    st.warning("⚠️ Please upload your `conversations.json` first on the home page.")
else:
    with st.spinner("Generating your 3D knowledge galaxy... 🌌"):
        fig = build_topic_graph(st.session_state["conversations"])
        st.plotly_chart(fig, use_container_width=True)
