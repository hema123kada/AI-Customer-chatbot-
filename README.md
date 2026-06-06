AI Customer Support Chatbot

A simple AI-powered Customer Support Chatbot built using RAG (Retrieval-Augmented Generation) and Google Gemini AI.

Files

Frontend
- index.html → Chatbot User Interface
- style.css → Styling and Design
- script.js → Frontend Logic and Backend Communication

Backend
- app.py → Flask Backend Server
- chatbot.py → Chatbot Response Logic
- rag.py → RAG Retrieval System
- config.py → Gemini API Configuration
- faq.txt → Knowledge Base for Customer Queries

---

Setup & Run

Step 1 — Install Required Packages

Open Terminal and run:

```bash
pip install flask flask-cors google-generativeai langchain faiss-cpu sentence-transformers
```

Step 2 — Add Gemini API Key

Open config.py and add your Gemini API key:

```python
GEMINI_API_KEY = "your_gemini_api_key"
```

Step 3 — Start Backend

```bash
cd backend
python app.py
```

You should see:

```bash
Running on http://127.0.0.1:5000
```

Step 4 — Open Frontend

Open:

```text
frontend/index.html
```

in your browser.

Step 5 — Start Chatting

Example Questions:

- What is your refund policy?
- What are your pricing plans?
- How can I contact support?
- What are your working hours?

---

## ⚙️ How It Works

1. User enters a query.
2. Frontend sends the query to Flask Backend.
3. RAG retrieves relevant information from FAQ data.
4. Gemini AI generates an intelligent response.
5. Response is displayed in the chatbot interface.

---

Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Google Gemini AI
- RAG (Retrieval-Augmented Generation)
- FAISS
- HuggingFace Embeddings

---

Future Enhancements

- Voice-enabled chatbot
- Multi-language support
- Database integration
- Cloud deployment
- Advanced AI-powered responses
