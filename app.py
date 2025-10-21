import streamlit as st
from data_loader import load_conversations

st.set_page_config(page_title="ChatGPT 3D History Model", layout="wide")

st.sidebar.markdown("📜 **How to export your ChatGPT data**")
st.sidebar.markdown("""
1. In ChatGPT, click your name → **Settings → Data Controls**  
2. Click **Export data → Export**  
3. You'll receive an email from OpenAI → Download the **.zip**  
4. Extract → locate **conversations.json**  
5. Upload that file below and wait for the graph to build!
""")

st.title("📁 Upload ChatGPT JSON")
uploaded_file = st.file_uploader("Upload your ChatGPT conversations.json", type="json")

if uploaded_file:
    st.session_state["conversations"] = load_conversations(uploaded_file)
    st.success("✅ File uploaded successfully! Go to **Topic Graph** from sidebar.")
