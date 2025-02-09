import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import numpy as np

# Load Excel data
file_path = 'data.xlsx'  # Replace with your Excel file path
df = pd.read_excel(file_path)

# Ensure the sheet has 'ID' and 'Context' columns
if 'ID' not in df.columns or 'Context' not in df.columns:
    raise ValueError("Excel sheet must contain 'ID' and 'Context' columns.")

# Load pre-trained sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')  # You can use other models as well

# Generate embeddings for all contexts in the Excel sheet
df['Embedding'] = df['Context'].apply(lambda x: model.encode(x))

# Function to retrieve relevant context based on query
def retrieve_context(query, top_n=3):
    query_embedding = model.encode(query).reshape(1, -1)
    
    # Stack embeddings for similarity computation
    context_embeddings = np.vstack(df['Embedding'].values)
    
    # Compute cosine similarity
    similarities = cosine_similarity(query_embedding, context_embeddings)[0]
    
    # Get top N similar contexts
    top_indices = similarities.argsort()[-top_n:][::-1]
    
    results = df.iloc[top_indices][['ID', 'Context']]
    return results

# Example Query
query = "How does Azure Policy enforce compliance?"
results = retrieve_context(query)

# Display Results
print("Top relevant contexts:\n")
for idx, row in results.iterrows():
    print(f"ID: {row['ID']}\nContext: {row['Context']}\n")
