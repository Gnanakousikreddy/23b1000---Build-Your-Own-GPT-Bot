from PyPDF2 import PdfReader
import requests
import json
import re

url = "http://localhost:11434/api/generate"

def read_pdf(pdf):
    text = ""
    pdf_reader = PdfReader(pdf)
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text

def clean_text(text) :
    text = re.sub(r'^\s*#{1,6}\s*', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{2,}', '\n\n', text)
    return text

def get_relevant_chunk(pdf_text, question, max_chars=2000):
    keywords = question.lower().split()
    paragraphs = pdf_text.split("\n\n")
    relevant = [p for p in paragraphs if any(word in p.lower() for word in keywords)]
    combined = "\n\n".join(relevant)
    return combined[:max_chars] 

pdf = read_pdf("Indian_Laws_and_Regulations.pdf")

cleaned_text = clean_text(pdf) 

while True :

    user_input = input("Input your query...\n")

    if user_input == "/bye" :
        break

    chunk = get_relevant_chunk(cleaned_text, user_input)

    prompt = f"""You are an Legal Advisor Bot that only answers based on the context below.
    If the answer is not in the context, respond only with 'I don't know'.

    Context:
    {chunk}

    User Question:
    {user_input}
    """

    payload = {
        "model": "tinyllama",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(url, json=payload)
    data = response.json()

    print("Answer:")
    if "response" in data and data["response"]:
        print(data["response"])
    elif "message" in data and "content" in data["message"]:
        print(data["message"]["content"])
    else:
        print("I don't know")

    print("-----------------------------------")