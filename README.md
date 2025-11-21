# 🧠 LLM Question-and-Answering System  
A simple NLP-powered Question & Answering system featuring:

- A **Python CLI application**
- A **Web GUI** (Flask-based)
- Integration with the **Hugging Face Inference API (Chat Completions)**
- Easy deployment on Render.com or other hosting platforms

---

## 🚀 Features
- Accept natural-language questions from users  
- Preprocess input (lowercasing, cleaning, math-friendly tokenization)  
- Forward processed question to an LLM through Hugging Face’s API  
- Display processed question, raw API output, and final answer  
- Clean modern web interface  
- Simple CLI interface  

---

## 📂 Project Structure

/LLM_QA_Project_YourName_MatricNo/
│── LLM_QA_CLI.py
│── app.py
│── requirements.txt
│── LLM_QA_hosted_webGUI_link.txt
│── .env
│── /static/
│ └── style.css
│── /templates/
└── index.html

---

## 🔧 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/LLM_QA_Project.git
cd LLM_QA_Project


🔐 2. Set Up Your Hugging Face API Key

Create a file named .env in the project root:

HUGGINGFACE_API_KEY=hf_xxxxxxxxxxxxxxxxx


The app automatically loads environment variables using python-dotenv.



📦 3. Install Dependencies

Run:

pip install -r requirements.txt


Typical requirements.txt:

Flask
requests
python-dotenv
gunicorn



🖥️ Running the CLI Application

Run:

python LLM_QA_CLI.py


Then type your question:

> Enter your question: what is 2+2?


The CLI will:

preprocess the question

send it to Hugging Face

print the final answer



🌐 Running the Web GUI (Flask App)

Start the Flask server:

python app.py


Then open this URL in your browser:

http://127.0.0.1:5000


You’ll be able to:

Enter a question

View the processed version

View the raw LLM response

See the final generated answer