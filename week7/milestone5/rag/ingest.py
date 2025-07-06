import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS


load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001",
                                          google_api_key = os.getenv("GEMINI_API_KEY"))


print("google genai embeddings loaded!!")

pdf_paths = [
    "data/ugrulebook.pdf",
]

all_documents = []

for pdf_path in pdf_paths :
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    all_documents.extend(documents)

print(f"Loaded {len(all_documents)} documents")

text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 100)

chunks = text_splitter.split_documents(all_documents)

print(f"Split into {len(chunks)} chunks")


vectorstore = FAISS.from_documents(chunks, embeddings)


vectorstore.save_local("vectorstore/faiss_index")
print("FAISS index saved to 'vectorstore/faiss_index'")