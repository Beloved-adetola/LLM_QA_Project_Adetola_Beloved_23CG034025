from flask import Flask, render_template, request
import re
import requests
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

def preprocess(text):
    text = text.lower()

    # Keep math operators: + - * / ^ = ( )
    text = re.sub(r'[^0-9a-zA-Z+\-*/^=().\s]', ' ', text)

    # Fix multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

API_URL = "https://router.huggingface.co/v1/chat/completions"

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

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    processed = ""
    raw_response = ""

    if request.method == "POST":
        question = request.form.get("question")
        processed = preprocess(question)
        prompt = f"Answer this question clearly:\n{processed}"

        raw_response = query_llm(prompt)
        answer = raw_response

    return render_template(
        "index.html",
        answer=answer,
        processed=processed,
        raw_response=raw_response
    )

if __name__ == "__main__":
    app.run(debug=True)
