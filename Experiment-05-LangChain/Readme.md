
# Experiment 5: LangChain Application Using Prompt Templates and Chains

## Aim

To create a basic LangChain application using PromptTemplate and chains for question answering.

## Objective

To understand how LangChain connects prompt templates with Large Language Models (LLMs) to develop question-answering applications.

## Theory

### What is LangChain?

LangChain is an open-source framework used to develop applications powered by Large Language Models (LLMs).

It provides tools for prompt management, model integration, chains, agents, memory, and retrieval-based applications.

### What is PromptTemplate?

A PromptTemplate is a reusable template that accepts input variables and generates structured prompts.

Example:

Template:
"Explain the following topic in simple words: {topic}"

Input:
"Artificial Intelligence"

Generated Prompt:
"Explain the following topic in simple words: Artificial Intelligence"

### What is a Chain?

A chain connects multiple components to execute a sequence of operations.

In this experiment, the chain connects:

1. PromptTemplate
2. Large Language Model
3. Output Parser

### Architecture

```text
User Question
     |
     v
PromptTemplate
     |
     v
Large Language Model
     |
     v
Output Parser
     |
     v
Final Answer
```

## Algorithm

1. Start the program.
2. Import the required LangChain libraries.
3. Initialize the Large Language Model.
4. Create a PromptTemplate with an input variable.
5. Connect the prompt, model, and output parser using a chain.
6. Accept a question from the user.
7. Pass the question to the chain.
8. Generate and display the answer.
9. Stop the program.

## Technologies Used

- Python 3
- LangChain
- OpenAI API
- PromptTemplate
- StrOutputParser

## Requirements

Install the required libraries:

```bash
pip install langchain-core langchain-openai python-dotenv
```

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload your actual API key to GitHub.

## How to Run

```bash
python main.py
```

## Expected Result

The application accepts a question, processes it using a LangChain prompt template and an LLM, and generates an appropriate answer.

## Advantages

1. Reusable prompt templates.
2. Simplified LLM integration.
3. Modular application development.
4. Easy integration with other LangChain components.
5. Support for automated question-answering workflows.

## Applications

- AI Chatbots
- Virtual Assistants
- Educational Question-Answering Systems
- Customer Support Applications
- Document-Based Question Answering

## Conclusion

This experiment demonstrates the implementation of a basic question-answering application using LangChain.

By combining PromptTemplate, a Large Language Model, and an output parser, the application generates structured and meaningful responses to user questions.
