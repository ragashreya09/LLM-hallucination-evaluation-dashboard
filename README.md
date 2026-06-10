# LLM-hallucination-evaluation-dashboard
A Streamlit-based GenAI dashboard to evaluate LLM responses for faithfulness, relevance, context grounding, unsupported claims, and hallucination risk.


# 🧠 LLM Evaluation and Hallucination Detection Dashboard

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-green)
![GenAI](https://img.shields.io/badge/GenAI-Evaluation-purple)
![Status](https://img.shields.io/badge/Status-Active-success)

A GenAI reliability dashboard that evaluates LLM-generated responses for **faithfulness, answer relevance, context relevance, unsupported claims, and hallucination risk**.

This project is designed for **RAG-based applications**, where LLM answers must be grounded in retrieved context before being trusted in production.

---

## 🚀 Project Overview

Large Language Models can generate fluent answers, but not all answers are factually grounded.  
This dashboard helps detect when an LLM response is **accurate, partially supported, or hallucinated**.

The system takes three inputs:

- ❓ User Question  
- 📄 Retrieved Context  
- 🤖 LLM Generated Answer  

Then it returns:

- ✅ Faithfulness Score  
- 🎯 Answer Relevance Score  
- 📚 Context Relevance Score  
- ⚠️ Hallucination Risk Level  
- 🔍 Unsupported Claims  
- 📝 Evaluation Explanation  

---

## ✨ Key Features

- 🧠 Evaluates LLM answers against retrieved context
- ⚠️ Detects hallucinated or unsupported claims
- 📊 Generates quality scores for RAG responses
- 🎯 Measures faithfulness, relevance, and context quality
- 📈 Displays interactive dashboard metrics and charts
- 📥 Exports evaluation results as CSV
- 🔐 Uses environment variables for API key security

---

## 🏗️ Architecture

```text
User Question
     │
     ▼
Retrieved Context + LLM Answer
     │
     ▼
Evaluation Prompt
     │
     ▼
OpenAI LLM Evaluator
     │
     ▼
Scores + Hallucination Risk + Unsupported Claims
     │
     ▼
Streamlit Dashboard
```

---

## 🛠️ Tech Stack

| Category | Tools |
|---|---|
| Programming | Python |
| Frontend | Streamlit |
| LLM | OpenAI |
| Data Handling | Pandas |
| Visualization | Plotly |
| Environment Management | python-dotenv |

---

## 📁 Project Structure

```text
llm-hallucination-evaluation-dashboard/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
│
├── src/
│   ├── evaluator.py
│   ├── prompts.py
│   └── utils.py
│
└── screenshots/
```

---

## ⚙️ How It Works

The dashboard compares the LLM answer with the retrieved context and checks whether the answer is actually supported.

### Evaluation Criteria

| Metric | Meaning |
|---|---|
| Faithfulness Score | Checks whether the answer is grounded in the context |
| Answer Relevance Score | Checks whether the answer directly responds to the question |
| Context Relevance Score | Checks whether the provided context is useful |
| Hallucination Risk | Classifies the answer as Low, Medium, or High risk |
| Unsupported Claims | Lists claims not supported by the context |

---

## 🧪 Sample Test Case

### ❓ User Question

```text
What is RAG and why is it useful?
```

### 📄 Retrieved Context

```text
Retrieval-Augmented Generation, or RAG, combines information retrieval with text generation.
It allows a language model to use external documents as grounding context before generating an answer.
This can improve factual accuracy and reduce unsupported responses.
```

### 🤖 LLM Answer

```text
RAG is a method that combines document retrieval with language generation.
It helps models generate more accurate answers by grounding responses in external context.
It is also used by NASA to train astronauts and can replace all traditional databases.
```

### ⚠️ Expected Evaluation

```text
Hallucination Risk: High

Unsupported Claims:
- Used by NASA to train astronauts
- Can replace all traditional databases
```

---

## 💻 Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/llm-hallucination-evaluation-dashboard.git
cd llm-hallucination-evaluation-dashboard
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For macOS/Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 6. Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📊 Dashboard Output

The app displays:

- Metric cards for faithfulness, relevance, and hallucination risk
- Bar chart for response evaluation scores
- Unsupported claim warnings
- LLM evaluator explanation
- CSV download option for evaluation records

---

## 🔮 Future Enhancements

- Add RAGAS evaluation metrics
- Add DeepEval integration
- Support batch evaluation from CSV files
- Add model comparison between GPT, Claude, and open-source LLMs
- Add FAISS or Pinecone-based retrieval pipeline
- Add Docker deployment
- Add Streamlit Cloud live demo
- Add evaluation history tracking

---

## 📌 Use Cases

- RAG chatbot evaluation
- Enterprise knowledge assistant testing
- Customer support bot quality checks
- Legal, healthcare, and finance document QA validation
- AI response quality monitoring
- GenAI reliability testing
---

## ⭐ Why This Project Matters

In production GenAI systems, generating an answer is not enough.  
The answer must be **grounded, reliable, explainable, and safe to use**.

This project focuses on one of the most important challenges in modern AI engineering:

> Can we trust the model’s answer?
