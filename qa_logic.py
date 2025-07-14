from transformers import pipeline

# Fast + lightweight models (optimized for CPU)
summarizer = pipeline("summarization", model="t5-small", device=-1)
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad", device=-1)

def summarize_text(text):
    trimmed_text = text[:700]  # keep it short for summarizer
    result = summarizer(trimmed_text)
    return result[0]['summary_text']

def ask_anything(prompt, context=""):
    if context:
        trimmed_context = context[:800]
        result = qa_pipeline(question=prompt, context=trimmed_context)
        return result['answer']
    return "Context required for QA."

def generate_challenge_questions():
    return [
        {"question": "What is the summary of the document?", "answer": "[Manual placeholder]"},
        {"question": "List two key takeaways.", "answer": "[Manual placeholder]"},
    ]

def evaluate_answer(user_response, correct_answer):
    if correct_answer in user_response:
        return "✅ Correct"
    elif user_response.strip() == "":
        return "❌ No Answer Provided"
    else:
        return "⚠️ Possibly Incomplete"
