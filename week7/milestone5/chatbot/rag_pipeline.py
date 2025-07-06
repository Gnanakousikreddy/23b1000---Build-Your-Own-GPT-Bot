import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate


load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

vectorstore = FAISS.load_local(
    "vectorstore/faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 4}
)

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    google_api_key=os.getenv("GEMINI_API_KEY")
)


prompt_template = """
You are an academic rule assistant for IIT Bombay's UG students.
Answer the question ONLY if it is relevant to the IITB UG rulebook or circulars.
If the question is irrelevant, politely say: "Sorry, I can only help with IIT Bombay's UG academic rules."

When you answer, DO NOT say things like "In the document it is mentioned" or "in the PDF you uploaded".
Just give a clear, student-friendly answer, referencing rules naturally.

Context:
{context}

Question:
{question}

Answer in a helpful, polite tone:
"""

rag_prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    chain_type_kwargs={"prompt": rag_prompt},
    return_source_documents=True
)

def run_query(user_query):
    result = qa_chain.invoke({"query": user_query})
    answer = result["result"]
    sources = result["source_documents"]
    return answer, sources

