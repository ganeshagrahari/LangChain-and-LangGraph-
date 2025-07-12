#chatmodels are used for generating text means : text -> text

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = 'text-generation',
    pipeline_kwargs=dict(
        temperature=0.1, # Adjust temperature for more or less randomness(means if temp is high model will generate more random text)
        max_new_tokens=100
    )

)

model = ChatHuggingFace(llm=llm)
result = model.invoke("WHat is the capital of India?")
print(result.content) 