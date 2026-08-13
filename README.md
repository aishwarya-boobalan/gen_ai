🤖 Local AI ChatGPT Clone with Ollama & Qwen2.5

A beginner-friendly Generative AI project to understand how an LLM-powered application actually works.

If you are new to Generative AI, don't just learn GenAI concepts from videos and theory—build something small and see the flow yourself.

This project is a simple ChatGPT-style chatbot built with:

🐍 Python

🎨 Streamlit

🦙 Ollama

🧠 Qwen2.5:3b

The goal is not to build a production ChatGPT clone.

The goal is to give a beginner a first glimpse into how a Generative AI application works from end to end.

🌱 Why should a GenAI beginner try this?

When you start learning Generative AI, you will hear terms like:

LLM

Prompt

System Prompt

API

Tokens

Temperature

Streaming

Conversation Memory

Local LLM

At first, these can feel like completely separate concepts.

This project connects them together in one small application.

Instead of only reading:

"An LLM generates a response based on the prompt."

you can actually see the flow:

User
  ↓
Streamlit Chat UI
  ↓
Python
  ↓
Ollama API
  ↓
Local LLM (Qwen2.5:3b)
  ↓
Generated response
  ↓
Streaming chunks
  ↓
Streamlit UI

That small flow gives you a hands-on glimpse of what happens inside a GenAI application.

🚀 What you will learn from this project

By building and understanding this chatbot, you get exposure to:

1. LLMs

You run a real language model locally using Ollama.

2. Prompting

You can provide a system prompt that controls how the assistant behaves.

3. API communication

Your Python application communicates with Ollama through:

http://localhost:11434/api/chat

4. Conversation memory

The application stores previous messages and sends the conversation history back to the model.

5. Streaming

Instead of waiting for the complete answer, the application receives the response in chunks and displays it progressively.

6. Temperature

You can change the model's response style using a temperature control.

7. Streamlit

You learn how to turn Python code into an interactive AI application.

🧠 How the application works

The core architecture is:

                    ┌─────────────────┐
                    │      User       │
                    │ "What is RAG?"  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │    Streamlit    │
                    │    Chat UI      │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │     Python      │
                    │ Build messages  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   Ollama API    │
                    │ localhost:11434 │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │   Qwen2.5:3b    │
                    │     Local LLM   │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Token/response  │
                    │     chunks      │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │    Streamlit    │
                    │  Shows answer   │
                    └─────────────────┘

The important thing to understand is that Streamlit is the UI, Python is the application logic, Ollama is the local model server, and Qwen2.5:3b is the LLM generating the response.

✨ Features

ChatGPT-style chat interface

Local LLM execution

Qwen2.5:3b support

Ollama model selection

Conversation memory using Streamlit session state

Streaming responses

Temperature control

Custom system prompt

Clear chat button

Ollama health check

Beginner-friendly teaching notes

🛠️ Prerequisites

You need:

Python 3.11+

Ollama

A downloaded Ollama model

Basic Python knowledge

This project uses:

Python 3.11
Streamlit
Ollama
Qwen2.5:3b

📥 Setup

1. Clone the repository

git clone <your-repository-url>
cd chatgpt_clone

2. Create a virtual environment

python -m venv env

3. Activate the environment

Windows PowerShell:

.\env\Scripts\Activate.ps1

You should see:

(env)

before your terminal prompt.

4. Install dependencies

python -m pip install streamlit requests

5. Install Ollama

Install Ollama on your system and verify:

ollama --version

6. Download Qwen2.5:3b

ollama pull qwen2.5:3b

Verify:

ollama list

You should see:

qwen2.5:3b

7. Run the application

streamlit run app.py

Then open the local URL shown by Streamlit, usually:

http://localhost:8501

🔍 Understanding the important parts

Ollama API

The application connects to Ollama using:

OLLAMA_URL = "http://localhost:11434/api/chat"

This means the model is running locally on your computer, rather than using a paid cloud API.

Sending a request

The application sends information such as:

payload = {
    "model": model,
    "messages": messages_for_ollama,
    "stream": True,
    "options": {
        "temperature": temperature
    }
}

This is where the application tells Ollama:

which model to use

what conversation to give the model

whether to stream the response

what temperature to use

Conversation memory

The project uses:

st.session_state.messages

to keep track of the conversation.

This helps demonstrate an important GenAI concept:

An LLM does not automatically know your previous conversation. The application can send the previous conversation history along with the new prompt.

🎯 What a beginner should do

Don't just copy-paste this project and call it done.

Try this learning approach:

Step 1 — Run it

Get the chatbot working.

Step 2 — Ask questions

Try:

What is Generative AI?
What is an LLM?
What is RAG?
Explain tokens.

Step 3 — Change the system prompt

Try changing:

You are a helpful AI assistant.

to:

You are a Python teacher who explains concepts using simple examples.

See how the responses change.

Step 4 — Change temperature

Try:

0.0
0.5
0.7
1.0

Observe how the responses differ.

Step 5 — Modify the UI

Change the title, colors, layout, and sidebar.

Step 6 — Break the code

This is important.

Change something and see what happens.

For example:

Remove the conversation history.

Turn streaming off.

Change the model.

Change the system prompt.

Remove the temperature option.

Then fix it.

That is where real learning happens.

💡 Why this project matters

You don't need to understand every advanced GenAI concept before building your first application.

Start small.

Run a model.

Send a prompt.

Receive a response.

Understand the API.

Understand the conversation history.

Understand streaming.

Then gradually build more advanced systems.

Build → Break → Understand → Improve.

That's the mindset this project is meant to encourage.

📌 Project goal

The goal of this repository is simple:

Help a beginner move from "I know what Generative AI is" to "I have built and understood a small Generative AI application."

If this project gives you your first glimpse of how an LLM application works, then it has done its job. 🚀