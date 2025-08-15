import streamlit as st                      # For building the interactive web UI of the 3D ChatGPT history model
import plotly.graph_objects as go           # For rendering the 3D visualization and interactive charts
import networkx as nx                       # For creating and managing the graph/network structure of chat history

# -------------------------------------------------------------------------------------------------------------------
from data_loader import load_conversations, get_title_text_map
from graph_builder import build_semantic_graph
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# -----------------------------
# Sidebar: How-to + Controls
# ----------------------------
st.sidebar.title("📜 How to export your ChatGPT data")
st.sidebar.markdown("""
1. In **ChatGPT**, click your name → **Settings** → **Data Controls**  
2. Click **Export data** → **Export**  
3. You'll receive an email from OpenAI → **Download** the `.zip`  
4. **Extract** the zip → locate `**conversations.json**`  
5. **Upload** that file below and wait for the graph to build!!!
""")

# Streamlit app title
st.title("ChatGPT Conversation Graph (Semantic Links)")

# File upload
uploaded_file = st.file_uploader("Upload ChatGPT JSON", type=["json"])

if uploaded_file is not None:
    # Load & process data
    conversations = load_conversations(uploaded_file)
    title_text_map = get_title_text_map(conversations)

    # Build graph
    G = build_semantic_graph(title_text_map, similarity_threshold=0.5)

    # Position nodes
    pos = nx.spring_layout(G, k=0.5, iterations=50)

    # Edges
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    # Nodes
    node_x, node_y, node_text = [], [], []
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(G.nodes[node]["label"])

    # Plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color="#888"),
        hoverinfo='none',
        mode='lines'
    ))
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=node_text,
        textposition="top center",
        hoverinfo='text',
        marker=dict(size=10, color='lightblue', line_width=2)
    ))

    st.plotly_chart(fig)
