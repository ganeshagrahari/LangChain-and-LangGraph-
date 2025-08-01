from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from typing import TypedDict
import os
import json
import re

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    temperature=0.1,
    max_new_tokens=300
)

model = ChatHuggingFace(llm=llm)

# Schema definition
class Review(TypedDict):
    summary: str
    sentiment: str

def extract_structured_output(response_text: str) -> dict:
    """Extract structured data from model response"""
    try:
        # Try to find JSON in the response
        json_match = re.search(r'\{[^{}]*\}', response_text)
        if json_match:
            json_str = json_match.group()
            return json.loads(json_str)
    except json.JSONDecodeError:
        pass
    
    # Fallback: Extract using regex patterns
    summary_pattern = r'(?:summary|Summary)["\':\s]*([^"\n}]+)'
    sentiment_pattern = r'(?:sentiment|Sentiment)["\':\s]*([^"\n}]+)'
    
    summary_match = re.search(summary_pattern, response_text, re.IGNORECASE)
    sentiment_match = re.search(sentiment_pattern, response_text, re.IGNORECASE)
    
    return {
        "summary": summary_match.group(1).strip().strip('"\'') if summary_match else "Unable to extract summary",
        "sentiment": sentiment_match.group(1).strip().strip('"\'') if sentiment_match else "neutral"
    }

def analyze_review(review_text: str) -> Review:
    """Analyze review and return structured output"""
    
    prompt = f"""
Analyze the following product review and provide a structured response in JSON format.

Review: {review_text}

Respond with ONLY a JSON object in this exact format:
{{
    "summary": "brief summary of the review highlighting key points",
    "sentiment": "positive"
}}

The sentiment should be one of: positive, negative, or neutral.

JSON Response:
"""
    
    try:
        # Get response from model
        response = model.invoke(prompt)
        
        # Extract structured data
        structured_data = extract_structured_output(response.content)
        
        return structured_data
        
    except Exception as e:
        print(f"Error during analysis: {e}")
        return {"summary": "Error processing review", "sentiment": "neutral"}

# Test with the Samsung Galaxy S24 Ultra review
review_text = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
"""

print("🔍 Analyzing Samsung Galaxy S24 Ultra Review...")
print("-" * 50)

result = analyze_review(review_text)

print("📊 Structured Output:")
print(f"📝 Summary: {result['summary']}")
print(f"😊 Sentiment: {result['sentiment']}")

print("\n" + "=" * 50)
print("✅ Analysis Complete!")
