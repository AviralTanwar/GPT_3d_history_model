import networkx as nx
from sentence_transformers import SentenceTransformer, util

def build_semantic_graph(title_text_map, similarity_threshold=0.5):
    """Builds a semantic similarity graph from title->text mapping."""
    model = SentenceTransformer("all-MiniLM-L6-v2")
    titles = list(title_text_map.keys())
    embeddings = model.encode(list(title_text_map.values()), convert_to_tensor=True)

    G = nx.Graph()

    # Add nodes
    for i, title in enumerate(titles):
        G.add_node(i, label=title)

    # Add edges based on similarity
    for i in range(len(titles)):
        for j in range(i + 1, len(titles)):
            sim = util.cos_sim(embeddings[i], embeddings[j]).item()
            if sim > similarity_threshold:
                G.add_edge(i, j, weight=sim)

    return G
