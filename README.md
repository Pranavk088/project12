GenAI Document Assistant
The GenAI Document Assistant is a web-based tool that allows users to upload PDF or TXT documents and interact with them using natural language. Users can ask questions about the content, receive AI-generated answers, summaries, and challenge themselves with logic-based questions.

🚀 Features
📄 Upload and parse PDF or TXT files

🧩 Document chunking and semantic embedding

🤖 Summarization using Hugging Face transformers

❓ Ask-anything QA mode

🧠 Challenge mode with custom logic-based questions

✅ AI evaluation of user answers

🛠️ Setup Instructions
🔧 Requirements
Python 3.8+

pip for installing packages

📦 Install Dependencies
Create a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Then install required packages:

bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, install manually:

bash
Copy
Edit
pip install streamlit fastapi uvicorn transformers faiss-cpu PyPDF2
▶️ Run the App
Make sure your backend and frontend are in the following structure:

markdown
Copy
Edit
project-root/
│
├── backend/
│   ├── __init__.py
│   ├── app.py
│   ├── document_processor.py
│   ├── embedding.py
│   └── qa_logic.py
│
├── frontend/
│   └── app.py
│
├── README.md
└── requirements.txt
To run the frontend Streamlit app:

bash
Copy
Edit
cd frontend
streamlit run app.py
🧠 Architecture / Reasoning Flow
📂 Document Flow
Upload File
User uploads .pdf or .txt file via Streamlit UI.

Document Parsing
Text is extracted using PyPDF2 or basic text reader.

Chunking & Embedding
The text is split into manageable chunks. Each chunk is embedded using Hugging Face models and indexed using FAISS for fast similarity search (if needed).

Summarization
The full document or chunks are summarized using sshleifer/distilbart-cnn-12-6 from Hugging Face.

Ask Anything Mode
Uses distilbert-base-uncased-distilled-squad to answer user queries based on context.

Challenge Me Mode
Presents user with logical questions. Their answers are evaluated using simple matching or model-based validation.

🧪 Models Used
Summarization: sshleifer/distilbart-cnn-12-6

Q&A: distilbert-base-uncased-distilled-squad

All models are served using Hugging Face’s transformers pipeline.

📁 Data Storage
Uploaded files are temporarily saved to data/

No files are permanently stored or shared

📌 Notes
This is a purely local application and no external API keys (e.g., OpenAI) are needed.

First-time model use will download weights (~500MB+).

Offline use is possible after initial model download.

