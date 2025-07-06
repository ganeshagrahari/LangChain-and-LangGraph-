#Embedding model are use to convert text to vector means : text -> vector(contexual understanding)
from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India."

vector = embeddings.embed_query(text)

print(str(vector))