from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model = 'textembedding-3-large', dimensions=32)
result = embeddings.embed_query("Delhi is the capital of India.")
print(str(result))
# result is a list of floats representing the embedding of the input text
# The length of the list is equal to the dimensions specified (32 in this case)
