
# Experiment 8: AI Agent Reflection Loop
# Agentic AI Laboratory
# Malla Reddy University

import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


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
# STEP 2: INITIALIZE LLM
# ---------------------------------------

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=api_key
)

output_parser = StrOutputParser()


# ---------------------------------------
# STEP 3: GENERATION PROMPT
# ---------------------------------------

generation_prompt = PromptTemplate(
    input_variables=["question"],
    template="""
You are a helpful AI educational assistant.

Answer the following question in simple English.

Question: {question}

Provide a clear and concise answer.
"""
)


# ---------------------------------------
# STEP 4: REFLECTION PROMPT
# ---------------------------------------

reflection_prompt = PromptTemplate(
    input_variables=["question", "answer"],
    template="""
You are an AI response reviewer.

Review the following answer.

Original Question:
{question}

Generated Answer:
{answer}

Evaluate the answer based on:

1. Accuracy
2. Clarity
3. Completeness
4. Relevance

Identify missing information and suggest
specific improvements.

Provide constructive feedback.
"""
)


# ---------------------------------------
# STEP 5: REVISION PROMPT
# ---------------------------------------

revision_prompt = PromptTemplate(
    input_variables=[
        "question",
        "answer",
        "feedback"
    ],
    template="""
You are an AI assistant improving a previous response.

Original Question:
{question}

Initial Answer:
{answer}

Reviewer Feedback:
{feedback}

Rewrite the answer using the feedback.

Requirements:
- Use simple English.
- Correct any identifiable mistakes.
- Include important missing information.
- Maintain clarity and relevance.
- Do not invent unsupported facts.

Improved Answer:
"""
)


# ---------------------------------------
# STEP 6: CREATE LANGCHAIN CHAINS
# ---------------------------------------

generation_chain = (
    generation_prompt
    | llm
    | output_parser
)

reflection_chain = (
    reflection_prompt
    | llm
    | output_parser
)

revision_chain = (
    revision_prompt
    | llm
    | output_parser
)


# ---------------------------------------
# STEP 7: REFLECTION AGENT FUNCTION
# ---------------------------------------

def reflection_agent(question):

    print("\nSTEP 1: GENERATING INITIAL RESPONSE")
    print("-" * 40)

    initial_answer = generation_chain.invoke({
        "question": question
    })

    print(initial_answer)

    print("\nSTEP 2: REFLECTING ON RESPONSE")
    print("-" * 40)

    feedback = reflection_chain.invoke({
        "question": question,
        "answer": initial_answer
    })

    print(feedback)

    print("\nSTEP 3: IMPROVING RESPONSE")
    print("-" * 40)

    improved_answer = revision_chain.invoke({
        "question": question,
        "answer": initial_answer,
        "feedback": feedback
    })

    print(improved_answer)

    return {
        "initial_answer": initial_answer,
        "feedback": feedback,
        "improved_answer": improved_answer
    }


# ---------------------------------------
# STEP 8: MAIN PROGRAM
# ---------------------------------------

print("EXPERIMENT 8: AI REFLECTION AGENT")
print("=" * 40)

question = input("\nEnter your question: ").strip()

if not question:
    print("Please enter a valid question.")

else:
    try:
        result = reflection_agent(question)

        print("\n" + "=" * 40)
        print("REFLECTION PROCESS COMPLETED")
        print("=" * 40)

        print("Initial Response: Generated")
        print("Feedback: Generated")
        print("Improved Response: Generated")

        print("\nExperiment completed successfully.")

    except Exception as error:
        print("\nError:", error)
        print("Check your API key and internet connection.")
