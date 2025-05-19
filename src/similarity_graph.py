from sklearn.neighbors import NearestNeighbors
import networkx as nx
import numpy as np

def build_graph(embeddings, threshold=0.85):
    embeddings_np = embeddings.cpu().numpy() if hasattr(embeddings, 'cpu') else embeddings

    # Use NearestNeighbors with cosine similarity
    nn = NearestNeighbors(metric='cosine', radius=1 - threshold)
    nn.fit(embeddings_np)
    distances, indices = nn.radius_neighbors(embeddings_np)

    G = nx.Graph()
    for i, neighbors in enumerate(indices):
        for j in neighbors:
            if i != j:
                G.add_edge(i, j)
    return G