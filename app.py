from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from backend import document_processor, embedding, qa_logic

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI backend is running!"}

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    text = await document_processor.read_text_from_file(file)
    chunks = embedding.split_into_chunks(text)
    index, chunk_list = embedding.create_faiss_index(chunks)
    return {"message": "File processed successfully.", "chunks": chunk_list}

@app.post("/ask")
async def ask_question(prompt: str = Form(...)):
    answer = qa_logic.ask_anything(prompt)
    return {"answer": answer}

@app.post("/challenge")
async def challenge():
    questions = qa_logic.generate_challenge_questions()
    return {"questions": questions}

@app.post("/evaluate")
async def evaluate(user_response: str = Form(...), correct_answer: str = Form(...)):
    result = qa_logic.evaluate_answer(user_response, correct_answer)
    return {"result": result}