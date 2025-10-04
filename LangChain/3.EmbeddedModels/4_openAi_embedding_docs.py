from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = 'textembedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India.",
    "Paris is the capital of France.",
    "Berlin is the capital of Germany."
]
results = embeddings.embed_documents(documents)
for result in results:
    print(str(result))
