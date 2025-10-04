from dotenv import load_dotenv
import openai
import os

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

print("🔑 OpenAI API Key Verification")
print("=" * 40)

# Check if API key exists
if not api_key:
    print("❌ ERROR: OPENAI_API_KEY not found in environment variables")
    print("💡 Make sure your .env file contains: OPENAI_API_KEY=your_key_here")
    exit(1)

# Display partial API key for verification (hide most characters for security)
if api_key.startswith('sk-'):
    masked_key = api_key[:7] + "*" * (len(api_key) - 11) + api_key[-4:]
    print(f"🔍 API Key Found: {masked_key}")
else:
    print(f"⚠️  WARNING: API key doesn't start with 'sk-': {api_key[:10]}...")

# Test 1: Basic API connection
print("\n📡 Test 1: Testing API Connection...")
try:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    
    # Simple completion test
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Say 'Hello, API is working!' and nothing else."}
        ],
        max_tokens=10
    )
    
    result = response.choices[0].message.content.strip()
    print(f"✅ SUCCESS: {result}")
    
except Exception as e:
    print(f"❌ FAILED: {str(e)}")
    print("\n🔧 Common issues:")
    print("   • Invalid API key")
    print("   • Insufficient credits/quota")
    print("   • Network connectivity issues")
    print("   • API key permissions")

# Test 2: Check available models
print("\n🤖 Test 2: Checking Available Models...")
try:
    models = client.models.list()
    gpt_models = [model.id for model in models.data if 'gpt' in model.id.lower()]
    
    print(f"✅ SUCCESS: Found {len(gpt_models)} GPT models")
    print("📋 Available GPT models:")
    for model in gpt_models[:5]:  # Show first 5
        print(f"   • {model}")
    if len(gpt_models) > 5:
        print(f"   ... and {len(gpt_models) - 5} more")
        
except Exception as e:
    print(f"❌ FAILED: {str(e)}")

# Test 3: Test with LangChain
print("\n🦜 Test 3: Testing with LangChain...")
try:
    from langchain_openai import ChatOpenAI
    
    # Create LangChain model
    model = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.1,
        api_key=api_key
    )
    
    # Test invocation
    response = model.invoke("What is 2+2? Answer with just the number.")
    print(f"✅ SUCCESS: LangChain response: {response.content}")
    
except Exception as e:
    print(f"❌ FAILED: {str(e)}")

# Test 4: Check account usage (if possible)
print("\n💰 Test 4: Checking Account Information...")
try:
    # Note: This endpoint might not be available in all API versions
    # Just attempt a simple call to verify billing is active
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hi"}],
        max_tokens=1
    )
    print("✅ SUCCESS: Account has active billing/credits")
    
except Exception as e:
    if "insufficient_quota" in str(e).lower():
        print("❌ FAILED: Insufficient quota/credits")
        print("💡 Solution: Add credits to your OpenAI account")
    elif "invalid" in str(e).lower():
        print("❌ FAILED: Invalid API key")
        print("💡 Solution: Check your API key in OpenAI dashboard")
    else:
        print(f"⚠️  WARNING: {str(e)}")

print("\n" + "=" * 40)
print("🏁 API Key Verification Complete!")

print("\n📝 Summary:")
print("• If all tests passed: Your API key is working perfectly! ✅")
print("• If some tests failed: Check the error messages above ⚠️")
print("• If all tests failed: Your API key might be invalid ❌")

print("\n🔗 Useful Links:")
print("• OpenAI API Dashboard: https://platform.openai.com/")
print("• API Key Management: https://platform.openai.com/api-keys")
print("• Usage & Billing: https://platform.openai.com/usage")
