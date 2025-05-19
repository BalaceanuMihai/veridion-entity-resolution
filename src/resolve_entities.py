import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx

print("Loading dataset...")
df = pd.read_csv("data/companies.csv")

print("Combining relevant fields...")
def build_text(row):
    return f"{row.get('company_name', '')} {row.get('short_description', '')} {row.get('product_type', '')}"

df['text'] = df.apply(build_text, axis=1)

print("Generating TF-IDF vectors...")
vectorizer = TfidfVectorizer().fit(df['text'])
vectors = vectorizer.transform(df['text'])

print("Computing cosine similarity matrix...")
similarity_matrix = cosine_similarity(vectors)

print("Building similarity graph...")
G = nx.Graph()
threshold = 0.85
for i in range(len(similarity_matrix)):
    for j in range(i + 1, len(similarity_matrix)):
        if similarity_matrix[i, j] > threshold:
            G.add_edge(i, j)

print("Extracting clusters...")
clusters = list(nx.connected_components(G))

print("Assigning canonical IDs...")
canonical_id_map = {}
for cluster in clusters:
    main_id = min(cluster)
    for idx in cluster:
        canonical_id_map[idx] = main_id

df['canonical_id'] = df.index.map(lambda i: canonical_id_map.get(i, i))

print("Sorting by canonical_id and rearranging columns...")
cols = ['canonical_id'] + [col for col in df.columns if col != 'canonical_id']
df = df[cols].sort_values(by='canonical_id')

print("Saving output to CSV...")
df.to_csv('data/resolved_companies.csv', index=False)
print("Entity resolution complete. Output saved to data/resolved_companies.csv")
