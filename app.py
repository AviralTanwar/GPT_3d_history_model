import streamlit as st
import json
import networkx as nx
import plotly.graph_objects as go

# --- UI Title ---
st.title("🧠 ChatGPT History: 3D Node Graph")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload your ChatGPT 'conversations.json'", type="json")
if not uploaded_file:
    st.info("Please upload your exported ChatGPT conversations.json file.")
    st.stop()

# --- Load JSON ---
data = json.load(uploaded_file)

# --- Create Graph ---
G = nx.DiGraph()

for conv in data:
    messages = conv.get("mapping", {})
    last_node = None

for key, msg in messages.items():
    message = msg.get("message")
    if not message:
        continue

    # Extract content parts safely
    parts = []
    if isinstance(message.get("content"), dict):
        parts = message["content"].get("parts", [])

    if parts:
        first_part = parts[0]
        if isinstance(first_part, str):
            content = first_part[:50]
        else:
            content = str(first_part)[:50]
    else:
        content = ""

    role = message.get("author", {}).get("role", "unknown")
    label = f"[{role}] {content}"

    G.add_node(key, label=label, role=role)

    if last_node:
        G.add_edge(last_node, key)

    last_node = key


# --- 3D Layout ---
pos = nx.spring_layout(G, dim=3, seed=42)

x_nodes = [pos[n][0] for n in G.nodes()]
y_nodes = [pos[n][1] for n in G.nodes()]
z_nodes = [pos[n][2] for n in G.nodes()]

edge_x, edge_y, edge_z = [], [], []

for edge in G.edges():
    x0, y0, z0 = pos[edge[0]]
    x1, y1, z1 = pos[edge[1]]
    edge_x += [x0, x1, None]
    edge_y += [y0, y1, None]
    edge_z += [z0, z1, None]

# --- Plotly 3D Graph ---
fig = go.Figure()

# Draw edges
fig.add_trace(go.Scatter3d(
    x=edge_x, y=edge_y, z=edge_z,
    mode='lines',
    line=dict(color='gray', width=1),
    hoverinfo='none'
))

# Draw nodes
fig.add_trace(go.Scatter3d(
    x=x_nodes, y=y_nodes, z=z_nodes,
    mode='markers+text',
    marker=dict(
        size=5,
        color=['blue' if G.nodes[n]['role'] == 'user' else 'green' for n in G.nodes()],
    ),
    text=[G.nodes[n]['label'] for n in G.nodes()],
    hoverinfo='text'
))

fig.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    showlegend=False,
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
    )
)

# --- Show in Streamlit ---
st.plotly_chart(fig, use_container_width=True)
