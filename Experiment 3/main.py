
# Experiment 3: Prompt Engineering Using LLMs
# Agentic AI Laboratory
# Malla Reddy University

import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please configure your .env file."
    )

# Initialize OpenAI client
client = OpenAI(api_key=api_key)


# Function to generate LLM responses
def generate_response(prompt):

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=0
    )

    return response.output_text


print("EXPERIMENT 3: PROMPT ENGINEERING")
print("=" * 40)


# ---------------------------------------
# 1. ZERO-SHOT PROMPTING
# ---------------------------------------

print("\n1. ZERO-SHOT PROMPTING")

zero_shot_prompt = """
Classify the sentiment of the following sentence
as Positive, Negative, or Neutral.

Sentence: I love learning Artificial Intelligence.

Return only the sentiment label.
"""

zero_shot_output = generate_response(
    zero_shot_prompt
)

print("Prompt:", zero_shot_prompt.strip())
print("Response:", zero_shot_output)


# ---------------------------------------
# 2. FEW-SHOT PROMPTING
# ---------------------------------------

print("\n2. FEW-SHOT PROMPTING")

few_shot_prompt = """
Classify the sentiment of the following sentences.

Examples:

Sentence: I love Python.
Sentiment: Positive

Sentence: This application is terrible.
Sentiment: Negative

Sentence: The weather is normal.
Sentiment: Neutral

Now classify:

Sentence: AI makes learning interesting.
Sentiment:
"""

few_shot_output = generate_response(
    few_shot_prompt
)

print("Prompt:", few_shot_prompt.strip())
print("Response:", few_shot_output)


# ---------------------------------------
# 3. CHAIN-OF-THOUGHT PROMPTING
# ---------------------------------------

print("\n3. CHAIN-OF-THOUGHT PROMPTING")

cot_prompt = """
A student has 5 books and buys 3 more books.

Each book costs Rs. 100.

Calculate the total value of all books.

Show a short step-by-step calculation
and provide the final answer.
"""

cot_output = generate_response(
    cot_prompt
)

print("Prompt:", cot_prompt.strip())
print("Response:", cot_output)


# ---------------------------------------
# FINAL COMPARISON
# ---------------------------------------

print("\n" + "=" * 40)
print("PROMPT ENGINEERING COMPARISON")
print("=" * 40)

print("\nZero-Shot Result:")
print(zero_shot_output)

print("\nFew-Shot Result:")
print(few_shot_output)

print("\nChain-of-Thought Result:")
print(cot_output)

print("\nExperiment completed successfully.")
