# Sampark-ai
An intelligent AI-powered content generation system built using LangChain and Groq LLMs.
This tool generates **high-converting, structured, and audience-targeted content** with built-in **content review and improvement capabilities**.

---

## 🚀 Features

* 🧠 AI-powered content generation (blogs, ads, emails, etc.)
* 🎯 Audience-targeted writing
* 🎨 Custom tone control (formal, casual, persuasive, etc.)
* ⚡ Fast inference using Groq LLM
* ✍️ Built-in **Content Reviewer Agent**
* 📈 Produces structured, high-converting output with CTA

---

## 🏗️ Tech Stack

* Python
* LangChain
* Groq LLM (`openai/gpt-oss-120b`)
* dotenv

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Uttamxalpha/Sampark-ai.git
cd Sampark-ai
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_api_key_here
```

⚠️ Never push `.env` to GitHub

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Then enter:

* Task type (e.g., ad copy, blog, email)
* Topic/Product
* Target audience
* Tone
* Extra instructions (optional)

---

## 🧠 How It Works

### 1. Writer Agent

* Uses structured prompt engineering
* Generates persuasive, high-quality content
* Ensures strong hook + CTA

### 2. Checker Agent

* Reviews generated content
* Identifies issues
* Improves clarity and effectiveness

---

## 📌 Example Use Cases

* Marketing copy
* LinkedIn posts
* Email campaigns
* Product descriptions
* Blog writing

---

## 🔐 Security Note

Sensitive data like API keys are stored in `.env`
and excluded using `.gitignore`

---

## 📈 Future Improvements

* Web UI (Streamlit / React)
* Multi-agent pipeline
* Memory integration
* Content scoring system

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📬 Contact

* GitHub: https://github.com/Uttamxalpha
* LinkedIn: https://linkedin.com/in/uttam-tiwari

---

⭐ If you found this useful, consider giving a star!
