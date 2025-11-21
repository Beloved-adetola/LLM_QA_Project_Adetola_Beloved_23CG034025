# LLM_QA_CLI.py
import re
import requests
import os
from dotenv import load_dotenv
load_dotenv()

# -----------------------------
# Basic text preprocessing
# -----------------------------
def preprocess(text):
    text = text.lower()

    # Keep math operators: + - * / ^ = ( )
    text = re.sub(r'[^0-9a-zA-Z+\-*/^=().\s]', ' ', text)

    # Fix multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# if not API_KEY:
#     return "No API key found. Set HUGGINGFACE_API_KEY environment variable."

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


API_URL = "https://router.huggingface.co/v1/chat/completions"

# -----------------------------
# Send prompt to an LLM API
# (HuggingFace Inference API used because it's free)
# -----------------------------
def query_llm(question):
    data = {
        "model": "meta-llama/Meta-Llama-3-8B-Instruct",
        "messages": [
            {"role": "user", "content": question}
        ],
        "max_tokens": 150
    }

    response = requests.post(API_URL, headers=headers, json=data)

    try:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    except Exception:
        return result

# -----------------------------
# Main CLI loop
# -----------------------------
def main():
    print("=== LLM Question & Answer CLI ===")
    print("Type 'exit' to quit.\n")

    while True:
        question = input("Enter your question: ")

        if question.lower() == "exit":
            print("Goodbye!")
            break

        processed = preprocess(question)
        prompt = f"Answer this question clearly:\n{processed}"

        print("\nSending to LLM...\n")
        answer = query_llm(prompt)

        print("------- Processed Question -------")
        print(processed)
        print("------- LLM Answer -------")
        print(answer)
        print("---------------------------------\n")

if __name__ == "__main__":
    main()
