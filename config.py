from openai import OpenAI

GROQ_API_KEY = "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"
MODEL_NAME = "llama-3.1-8b-instant"

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1")