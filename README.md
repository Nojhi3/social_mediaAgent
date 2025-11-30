# 🎨 Social Media Content Generation Agent

An AI-powered agent that generates creative social media content ideas, captions, analyzes trends, creates posting schedules, and retrieves past content using Google Gemini API, LangChain, ChromaDB, and Gradio.

![Agent Demo](https://img.shields.io/badge/Status-Active-success)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)
![Gradio](https://img.shields.io/badge/Gradio-Latest-orange)

## ✨ Features

- **🎯 Content Idea Generator**: Generate 5 unique, platform-specific content ideas for any topic or niche
- **✍️ Caption Writer**: Create engaging captions in 3 styles (short/punchy, storytelling, long-form with CTA)
- **📊 Trend Analyzer**: Analyze current social media trends with hashtag recommendations and posting times
- **📅 Post Scheduler**: Generate 7-day content calendars with strategic posting plans
- **💾 Content Retriever (RAG)**: Store and retrieve past content using ChromaDB vector database

## 🚀 Live Demo

Try it out: [Hugging Face Space Link](your-space-url-here)

## 🛠️ Tech Stack

- **LLM**: Google Gemini 1.5 Pro via LangChain
- **Framework**: LangChain for agent orchestration
- **Vector DB**: ChromaDB for content storage and retrieval
- **Embeddings**: HuggingFace Sentence Transformers (all-MiniLM-L6-v2)
- **UI**: Gradio ChatInterface
- **Deployment**: Hugging Face Spaces

## 📋 Prerequisites

- Python 3.10 or higher
- Google Gemini API Key ([Get it here](https://makersuite.google.com/app/apikey))
- 2GB+ RAM (for embedding model)

## 💻 Running Locally - Complete Guide

git clone https://github.com/Nojhi3/social_mediaAgent
cd social_mediaAgent

### Step 2: Create Virtual Environment (Recommended)

**On Windows:**
python -m venv venv
venv\Scripts\activate

### Step 3: Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

### Step 4: Get Your Google Gemini API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated API key

**Note:** Gemini API has a generous free tier perfect for development.

### Step 5: Set Up API Key

Choose one of these methods:

**Option A: Environment Variable (Recommended)**

**Windows (Command Prompt):**
set GOOGLE_API_KEY=your_gemini_api_key_here

### Step 6: Run the Application

python app.py

You should see output like:
Running on local URL: http://0.0.0.0:7860

### Step 1: Clone the Repository

