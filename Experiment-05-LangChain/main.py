
# Experiment 5: LangChain Application
# Using PromptTemplate and Chains
# Agentic AI Laboratory
# Malla Reddy University

import os
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI


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
# STEP 2: INITIALIZE THE LLM
# ---------------------------------------

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=api_key
)


# ---------------------------------------
# STEP 3: CREATE PROMPT TEMPLATE
# ---------------------------------------

prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful AI educational assistant.

Answer the following question in simple
and easy-to-understand English.

Question: {question}

Answer:
"""
)


# ---------------------------------------
# STEP 4: CREATE OUTPUT PARSER
# ---------------------------------------

output_parser = StrOutputParser()


# ---------------------------------------
# STEP 5: CREATE LANGCHAIN CHAIN
# ---------------------------------------

chain = prompt | llm | output_parser


# ---------------------------------------
# STEP 6: QUESTION ANSWERING
# ---------------------------------------

print("EXPERIMENT 5: LANGCHAIN APPLICATION")
print("=" * 40)

question = input("\nEnter your question: ").strip()

if not question:
    print("Please enter a valid question.")
else:
    print("\nProcessing your question...")

    try:
        response = chain.invoke({
            "question": question
        })

        print("\nQuestion:", question)
        print("\nGenerated Answer:")
        print(response)

        print("\nExperiment completed successfully.")

    except Exception as error:
        print("\nError:", error)
        print("Please check your API key and internet connection.")
