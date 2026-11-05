
# Experiment 9: Retrieval-Augmented Generation
# Agentic AI Laboratory
# Malla Reddy University

import os
from pathlib import Path

from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import (
    ChatOpenAI,
    OpenAIEmbeddings
)

from langchain_chroma import Chroma

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


# ---------------------------------------
# STEP 1: LOAD ENVIRONMENT VARIABLES
# ---------------------------------------

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please configure your .env file."
    )


# ---------------------------------------
# STEP 2: LOAD SAMPLE DOCUMENT
# ---------------------------------------

base_dir = Path(__file__).resolve().parent

document_path = base_dir / "sample_document.txt"

if not document_path.exists():
    raise FileNotFoundError(
        "sample_document.txt not found."
    )

with open(document_path, "r", encoding="utf-8") as file:
    document_text = file.read()

documents = [
    Document(
        page_content=document_text,
        metadata={"source": "sample_document.txt"}
    )
]

print("EXPERIMENT 9: RAG SYSTEM")
print("=" * 40)

print("\nDocument loaded successfully.")


# ---------------------------------------
# STEP 3: SPLIT DOCUMENT INTO CHUNKS
# ---------------------------------------

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = text_splitter.split_documents(documents)

print("Number of document chunks:", len(chunks))


# ---------------------------------------
# STEP 4: INITIALIZE EMBEDDING MODEL
# ---------------------------------------

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    api_key=api_key
)


# ---------------------------------------
# STEP 5: CREATE CHROMA VECTOR DATABASE
# ---------------------------------------

vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="agentic_ai_lab_exp9"
)

print("Vector database created successfully.")


# ---------------------------------------
# STEP 6: INITIALIZE RETRIEVER
# ---------------------------------------

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)


# ---------------------------------------
# STEP 7: INITIALIZE LLM
# ---------------------------------------

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=api_key
)


# ---------------------------------------
# STEP 8: CREATE PROMPT TEMPLATE
# ---------------------------------------

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a helpful AI educational assistant.

Answer the question using only the
provided document context.

If the answer is not present in the
context, say:

"I could not find the answer in the document."

Context:
{context}

Question:
{question}

Answer:
"""
)


# ---------------------------------------
# STEP 9: CREATE RAG CHAIN
# ---------------------------------------

rag_chain = (
    prompt
    | llm
    | StrOutputParser()
)


# ---------------------------------------
# STEP 10: ACCEPT USER QUESTION
# ---------------------------------------

question = input("\nEnter your question: ").strip()

if not question:
    print("Please enter a valid question.")

else:
    try:
        print("\nRetrieving relevant documents...")

        retrieved_docs = retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content
            for doc in retrieved_docs
        )

        print("\nRetrieved Document Chunks:")

        for index, doc in enumerate(
            retrieved_docs, start=1
        ):
            print(f"\nChunk {index}:")
            print(doc.page_content)
            print(
                "Source:",
                doc.metadata.get("source", "Unknown")
            )

        print("\nGenerating answer...")

        answer = rag_chain.invoke({
            "context": context,
            "question": question
        })

        print("\n" + "=" * 40)
        print("FINAL RAG ANSWER")
        print("=" * 40)

        print("\nQuestion:", question)
        print("\nAnswer:", answer)

        print("\nSource: sample_document.txt")

        print("\nExperiment completed successfully.")

    except Exception as error:
        print("\nError:", error)
        print("Check API key, dependencies, and connection.")
