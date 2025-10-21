import plotly.graph_objects as go
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer
import numpy as np

def build_topic_graph(conversations):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    titles = list(conversations.keys())
    texts = list(conversations.values())

    embeddings = model.encode(texts)
    reduced = TSNE(n_components=2, random_state=42).fit_transform(embeddings)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=reduced[:,0],
        y=reduced[:,1],
        mode='markers+text',
        text=titles,
        textposition='top center',
        marker=dict(
            size=8,
            color='#00ff99',  # neon green
            line=dict(width=1, color='#00ffaa'),
        ),
        hovertemplate='%{text}<extra></extra>'
    ))

    fig.update_layout(
        paper_bgcolor="#0a0f1a",
        plot_bgcolor="#0a0f1a",
        font=dict(color="#e2e8f0"),
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0)
    )

    return fig
