# 🦜🔗 LangChain Framework - Complete Learning Guide

A comprehensive collection of **LangChain** examples and implementations covering core concepts, chat models, embeddings, and prompt engineering. This repository serves as a hands-on learning resource for building AI-powered applications with LangChain.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Environment Setup](#-environment-setup)
- [Usage Examples](#-usage-examples)
- [Components Overview](#-components-overview)
- [API Keys Required](#-api-keys-required)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🤖 Multiple LLM Integrations**: OpenAI, Anthropic, Google Gemini, Hugging Face
- **💬 Interactive Chatbots**: Conversation-aware chatbots with memory
- **🔍 Embedding Models**: Document similarity and semantic search
- **📝 Dynamic Prompts**: Template-based prompt generation
- **🎯 Message Handling**: Proper conversation flow with SystemMessage, HumanMessage, AIMessage
- **� Structured Output**: Type-safe responses with TypedDict and Pydantic
- **🔧 API Testing**: Built-in tools to verify API keys and connections
- **🛠️ Error Handling**: Robust error management and fallback strategies
- **�📚 Learning Examples**: Step-by-step implementations for beginners

## 📁 Project Structure

```
LangChain-Framework/
├── 📂 1.LLMs/                     # Large Language Model examples
│   └── 1_llm_demo.py              # Basic LLM usage with OpenAI
├── 📂 2.ChatModels/               # Chat model implementations
│   ├── 1_chatmodel_hf_api.py      # Hugging Face API chat model
│   └── 2_chatmodel_hf_local.py    # Local Hugging Face model
├── 📂 3.EmbeddedModels/          # Embedding and similarity examples
│   ├── 1_embeddingmodel_hf_local.py    # Local Hugging Face embeddings
│   ├── 2_Document_Similarity.py        # Document similarity analysis
│   ├── 3_openAi_embedding_modes.py     # OpenAI embedding models
│   └── 4_openAi_embedding_docs.py      # OpenAI document embeddings
├── 📂 4.Prompt/                  # Prompt engineering examples
│   ├── Prompt_generator.py       # Dynamic prompt generation
│   ├── prompt_ui.py             # UI for prompt creation
│   ├── chat_prompt_template.py  # Chat prompt templates
│   ├── message_placeholdder.py  # Message placeholders
│   ├── messages.py             # Message handling examples
│   └── chat_history.txt        # Sample conversation data
├── � 5.Structured_Output_Langchain/ # Structured output examples
│   ├── typeddict_demp.py        # TypedDict demonstration
│   └── with_structured_output_typedict.py # Structured output with TypedDict
├── 📄 chatbot.py                # Full-featured chatbot with conversation history
├── 📄 structured_output_alternative.py # Alternative structured output for HF models
├── 📄 structured_output_openai.py      # OpenAI structured output example
├── 📄 with_structured_output_typedict.py # Main structured output example
├── 📄 test_openai_api.py        # OpenAI API key verification tool
├── 📄 requirements.txt          # Python dependencies
└── 📄 template.json            # Configuration templates
```

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ganeshagrahari/Langchain-Framework.git
cd Langchain-Framework
```

### 2. Create Virtual Environment
```bash
# Create virtual environment
python -m venv langchain-env

# Activate virtual environment
# On Linux/macOS:
source langchain-env/bin/activate
# On Windows:
# langchain-env\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔧 Environment Setup

Create a `.env` file in the root directory with your API keys:

```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# Hugging Face API Token
HUGGINGFACEHUB_ACCESS_TOKEN=your_huggingface_token_here

# Anthropic API Key (Optional)
ANTHROPIC_API_KEY=your_anthropic_api_key_here

# Google API Key (Optional)
GOOGLE_API_KEY=your_google_api_key_here
```

## 🚀 Usage Examples

### Basic LLM Usage
```python
# Run basic LLM example
python 1.LLMs/1_llm_demo.py
```

### Interactive Chatbot
```python
# Run the conversational chatbot
python chatbot.py
```

### Document Similarity
```python
# Test document similarity
python 3.EmbeddedModels/2_Document_Similarity.py
```

### Dynamic Prompt Templates
```python
# Create dynamic prompts
python 4.Prompt/chat_prompt_template.py
```

### Structured Output Examples
```python
# OpenAI structured output (recommended)
python structured_output_openai.py

# Alternative approach for Hugging Face models
python structured_output_alternative.py

# TypedDict demonstration
python 5.Structured_Output_Langchain/typeddict_demp.py
```

### API Key Verification
```python
# Test your OpenAI API key
python test_openai_api.py
```

## 🧩 Components Overview

### 1. 🤖 LLMs (Large Language Models)
- **Basic LLM Usage**: Simple question-answering with OpenAI GPT models
- **Text Generation**: Generate creative content and responses

### 2. 💬 Chat Models
- **Hugging Face API**: Use cloud-hosted models via API
- **Local Models**: Run models locally for privacy and cost efficiency
- **Conversation Management**: Handle multi-turn conversations

### 3. 🔍 Embedding Models
- **Text Embeddings**: Convert text to vector representations
- **Document Similarity**: Compare documents semantically
- **Semantic Search**: Find relevant content based on meaning

### 4. 📝 Prompt Engineering
- **Template-based Prompts**: Create reusable prompt templates
- **Dynamic Variables**: Inject context-specific information
- **Message Placeholders**: Handle conversation history in prompts

### 5. 🗣️ Chatbot Features
- **Memory Management**: Maintain conversation context
- **Message Types**: SystemMessage, HumanMessage, AIMessage
- **Error Handling**: Robust error management
- **User Experience**: Interactive command-line interface

### 6. 📊 Structured Output
- **TypedDict Support**: Type-safe data structures
- **Multiple Approaches**: OpenAI native vs. prompt-engineering fallbacks
- **JSON Parsing**: Robust extraction from model responses
- **Error Recovery**: Fallback strategies for parsing failures

## 🔑 API Keys Required

| Service | Required For | How to Get |
|---------|--------------|------------|
| **OpenAI** | GPT models, OpenAI embeddings | [OpenAI Platform](https://platform.openai.com/) |
| **Hugging Face** | Hugging Face models | [Hugging Face Tokens](https://huggingface.co/settings/tokens) |
| **Anthropic** | Claude models | [Anthropic Console](https://console.anthropic.com/) |
| **Google** | Gemini/PaLM models | [Google AI Studio](https://makersuite.google.com/) |

## 🎯 Key Learning Points

1. **LangChain Basics**: Understanding core concepts and abstractions
2. **Model Integration**: Working with different LLM providers
3. **Prompt Engineering**: Creating effective prompts for better outputs
4. **Memory Management**: Implementing conversation memory
5. **Structured Output**: Type-safe responses and data extraction
6. **Error Handling**: Building robust AI applications
7. **API Management**: Testing and verifying API connections
8. **Production Ready**: Best practices for deployment

## 📊 Supported Models

### LLM Providers
- ✅ **OpenAI**: GPT-3.5, GPT-4
- ✅ **Hugging Face**: Llama, Mistral, CodeLlama
- ✅ **Anthropic**: Claude
- ✅ **Google**: Gemini, PaLM

### Embedding Models
- ✅ **OpenAI**: text-embedding-ada-002
- ✅ **Hugging Face**: sentence-transformers
- ✅ **Local Models**: Custom embeddings

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) for the amazing framework
- [Hugging Face](https://huggingface.co/) for open-source models
- [OpenAI](https://openai.com/) for powerful language models

## 📬 Contact

- **GitHub**: [@ganeshagrahari](https://github.com/ganeshagrahari)
- **Repository**: [Langchain-Framework](https://github.com/ganeshagrahari/Langchain-Framework)

---

⭐ **Star this repository if you find it helpful!** ⭐

*Happy Learning with LangChain! 🦜🔗*
