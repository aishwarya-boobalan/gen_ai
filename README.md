# 🤖 Local AI ChatGPT Clone

### A beginner-friendly Generative AI project to understand how an LLM-powered application works.

> **Don't just learn GenAI. Build it. Run it. Understand it.**

This project is a simple ChatGPT-style chatbot built with:

- 🐍 Python
- 🎨 Streamlit
- 🦙 Ollama
- 🧠 Qwen2.5:3b

The goal is not to build a production-level ChatGPT clone.

The goal is to give a beginner a **practical glimpse into how a Generative AI application works end-to-end.**

---

## 🧠 GenAI Flow

```text
        👤 User
           │
           ▼
   🎨 Streamlit UI
           │
           ▼
      🐍 Python
           │
           │ HTTP Request
           ▼
     🦙 Ollama API
           │
           ▼
    🧠 Qwen2.5:3b
           │
           │ Generated Response
           ▼
      ⚡ Streaming
           │
           ▼
   🎨 Streamlit UI
```

### In simple words

```text
User asks a question
        ↓
Streamlit collects it
        ↓
Python prepares the request
        ↓
Ollama receives the request
        ↓
Qwen2.5:3b generates the response
        ↓
Response is streamed back
        ↓
Streamlit displays the answer
```

This gives a beginner a **first practical glimpse of how the different parts of a GenAI application connect together.**

---

## 🔗 What Each Component Does

### 🎨 Streamlit

Creates the chatbot interface.

It allows you to:

- Type questions
- See chat messages
- Select models
- Change temperature
- Modify the system prompt

### 🐍 Python

Acts as the **bridge between the UI and the LLM**.

It handles:

- User input
- Conversation history
- API requests
- Responses

### 🦙 Ollama

Ollama is the **local LLM runtime/server**.

Instead of sending your prompt to a cloud AI provider, Ollama allows the model to run locally on your computer.

The application communicates with Ollama through:

```text
http://localhost:11434/api/chat
```

### 🧠 Qwen2.5:3b

This is the actual **language model** generating the responses.

Ollama runs the model, while **Qwen is the model doing the language generation**.

---

## 💡 GenAI Concepts Demonstrated

This project gives you hands-on exposure to:

- 🤖 LLMs
- 💬 Prompting
- 📝 System prompts
- 🔗 API communication
- 🧠 Conversation memory
- ⚡ Streaming responses
- 🌡️ Temperature
- 🦙 Local LLM inference

---

## ✨ Features

- 🤖 ChatGPT-style chat interface
- 🧠 Local LLM execution
- 🦙 Ollama integration
- 🧠 Qwen2.5:3b support
- 💬 Conversation memory
- ⚡ Streaming responses
- 🌡️ Temperature control
- 📝 Custom system prompt
- 🧹 Clear chat
- ❤️ Ollama health check

---

## 🛠️ Tech Stack

```text
Python
   │
   ├── Streamlit
   ├── Requests
   │
   └── Ollama API
          │
          └── Qwen2.5:3b
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd chatgpt_clone
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\env\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install streamlit requests
```

### 5. Check Ollama

Make sure Ollama is installed:

```bash
ollama --version
```

### 6. Download Qwen2.5:3b

```bash
ollama pull qwen2.5:3b
```

Verify the model:

```bash
ollama list
```

You should see:

```text
qwen2.5:3b
```

### 7. Run the application

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

🎉 **Your local AI chatbot is ready!**

---

## 🔍 How the LLM Request Works

One of the most important parts of the application is:

```python
payload = {
    "model": model,
    "messages": messages_for_ollama,
    "stream": True,
    "options": {
        "temperature": temperature
    }
}
```

This tells Ollama:

```text
Which model?
      ↓
qwen2.5:3b

What should it know?
      ↓
Conversation history

How should it respond?
      ↓
System prompt + temperature

How should the response arrive?
      ↓
Streaming
```

Python then sends the request:

```python
requests.post(
    OLLAMA_URL,
    json=payload,
    stream=True
)
```

The overall flow becomes:

```text
Python
   ↓
HTTP POST
   ↓
Ollama API
   ↓
Qwen2.5:3b
   ↓
Response chunks
   ↓
Python
   ↓
Streamlit
```

---

## 🎯 Explore the Application

Try different prompts:

```text
What is Generative AI?
```

```text
What is an LLM?
```

```text
Explain tokens.
```

```text
Explain RAG to a beginner.
```

Experiment with the **system prompt** and see how the model's behavior changes.

Try different **temperature values**:

```text
0.0
0.5
0.7
1.0
```

You can also experiment by changing the model, UI, conversation history, or streaming behavior.

> **The best way to understand GenAI is not just to read about it — it's to interact with the complete flow.**

---

## 🌟 Why This Project?

You don't need to understand every advanced GenAI concept before building your first AI application.

Start with something small:

```text
Run a model
     ↓
Send a prompt
     ↓
Get a response
     ↓
Understand the API
     ↓
Understand memory
     ↓
Understand streaming
```

Once you see this flow working on your own computer, concepts that initially seem abstract become much easier to understand.

---

## 📌 Project Goal

The goal of this repository is simple:

> **Help a beginner move from "I know what Generative AI is" to "I have built and understood a small Generative AI application."**

This project is your **first practical glimpse into the world of Generative AI.** 🤖🚀

---

### ⭐ If you're just starting GenAI, build this first.

**Run it → Explore it → Understand it.**

> **Your first GenAI application doesn't need to be complicated. It just needs to show you how the pieces connect.**
