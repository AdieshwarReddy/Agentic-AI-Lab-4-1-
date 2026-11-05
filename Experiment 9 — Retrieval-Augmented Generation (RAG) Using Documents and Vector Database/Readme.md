
# Experiment 9: Retrieval-Augmented Generation (RAG) Using Documents and Vector Database

## Aim

To create a Retrieval-Augmented Generation (RAG) system using documents and a vector database.

## Objective

To understand how RAG combines document retrieval with Large Language Models (LLMs) to generate answers based on relevant external knowledge.

## Theory

### What is Retrieval-Augmented Generation?

Retrieval-Augmented Generation (RAG) is an AI technique that improves LLM responses by retrieving relevant information from external knowledge sources before generating answers.

Instead of relying only on the model's training knowledge, RAG supplies relevant document content to the LLM.

### Components of RAG

**1. Document Loading**

Loads information from text files, PDFs, databases, or other sources.

**2. Text Splitting**

Divides large documents into smaller chunks for efficient processing.

**3. Embeddings**

Converts text chunks into numerical vector representations that capture semantic meaning.

**4. Vector Database**

Stores document embeddings and supports similarity-based retrieval.

**5. Retriever**

Searches the vector database to find relevant document chunks for a user question.

**6. Large Language Model**

Generates an answer using the retrieved document context.

## RAG Architecture

```text
             DOCUMENT PROCESSING

           Input Text Document
                    |
                    v
              Text Splitting
                    |
                    v
             Generate Embeddings
                    |
                    v
             Chroma Vector DB


               QUERY PROCESSING

               User Question
                    |
                    v
              Query Embedding
                    |
                    v
             Similarity Search
                    |
                    v
           Relevant Document Chunks
                    |
                    v
              Prompt Template
                    |
                    v
               OpenAI LLM
                    |
                    v
                Final Answer
```

## Problem Statement

Develop a document-based question-answering system that:

1. Loads a sample text document.
2. Splits the document into smaller chunks.
3. Converts the chunks into embeddings.
4. Stores embeddings in a Chroma vector database.
5. Accepts a user question.
6. Retrieves relevant document chunks.
7. Generates an answer using an LLM.
8. Displays the answer and retrieved sources.

## Algorithm

1. Start the program.
2. Import the required Python libraries.
3. Load the OpenAI API key.
4. Read the sample document.
5. Split the document into chunks.
6. Generate embeddings using an embedding model.
7. Store the embeddings in ChromaDB.
8. Accept a user question.
9. Retrieve the most relevant chunks.
10. Create a prompt using the retrieved context.
11. Generate an answer using the LLM.
12. Display the answer and source information.
13. Stop the program.

## Technologies Used

- Python 3
- LangChain
- OpenAI API
- ChromaDB
- OpenAI Embeddings
- PromptTemplate
- Retrieval-Augmented Generation

## Requirements

Install the required Python packages:

```bash
pip install langchain-core langchain-openai langchain-chroma langchain-text-splitters python-dotenv
```

Create a `.env` file in the repository root:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload your actual API key to GitHub.

## How to Run

Open a terminal in the Experiment-09-RAG folder.

Run:

```bash
python main.py
```

Enter a question related to the sample document.

Example:

What is Retrieval-Augmented Generation?

## Expected Result

The application retrieves relevant document content from ChromaDB and generates an answer using the OpenAI LLM.

The output includes:

- User Question
- Retrieved Document Chunks
- Generated Answer
- Source Document

## Advantages

1. Provides document-grounded answers.
2. Integrates external knowledge with LLMs.
3. Supports semantic search.
4. Can reduce hallucinations when relevant context is retrieved.
5. Supports question answering over custom documents.

## Limitations

1. Requires good-quality documents.
2. Retrieval may return irrelevant chunks.
3. LLM answers may still contain inaccuracies.
4. API usage may incur costs.
5. Retrieval quality depends on embeddings and chunking.

## Applications

- Document Question Answering
- Educational Chatbots
- Research Assistants
- Enterprise Knowledge Search
- Customer Support Systems
- Legal Document Analysis
- Healthcare Information Retrieval

## Conclusion

This experiment demonstrates a basic Retrieval-Augmented Generation system using LangChain, OpenAI, and ChromaDB.

The system loads a document, generates embeddings, stores them in a vector database, retrieves relevant content, and generates context-based answers.

RAG helps connect LLM applications with external knowledge sources.
