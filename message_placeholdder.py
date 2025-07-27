from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

#chat template
chat_template = ChatPromptTemplate([
    
        ('system','you are a  helpful Customer support Agent.'),
        MessagesPlaceholder(variable_name='chat_history'),
        ('human','{query}')
    
])

chat_history = []

#load chathistory
with open('chat_history.txt') as f :
    chat_history.extend(f.readlines())

print(chat_history)    
#cretae prmpt

prompt = chat_template.invoke({'chat_history':chat_history,'query':'Where is my refund?'})

print(prompt)