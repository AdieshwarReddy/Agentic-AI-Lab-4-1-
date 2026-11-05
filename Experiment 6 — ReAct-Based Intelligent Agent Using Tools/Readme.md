
# Experiment 6: ReAct-Based Intelligent Agent Using Tools

## Aim

To develop a ReAct-based intelligent agent that uses tools such as a calculator or search to solve user queries through reasoning and action.

## Objective

To understand how an AI agent combines reasoning, tool selection, action execution, and observations to solve problems.

## Theory

### What is ReAct?

ReAct stands for Reasoning and Acting.

It is an AI agent framework that combines reasoning with actions performed through external tools.

Instead of generating an answer directly, a ReAct agent can select a tool, execute an action, observe the result, and continue until it produces a final answer.

### ReAct Workflow

```text
        User Query
            |
            v
       AI Agent (LLM)
            |
            v
       Select Action
            |
            v
       Execute Tool
            |
            v
       Observe Result
            |
            v
    Continue or Finish?
       /          \
    Continue      Finish
       |             |
       v             v
    AI Agent     Final Answer
```

### Components of a ReAct Agent

1. **Reasoning:** Determines what information or calculation is required.
2. **Action:** Selects and calls an appropriate tool.
3. **Observation:** Receives the result returned by the tool.
4. **Iteration:** Repeats tool usage if necessary.
5. **Final Answer:** Generates a response based on the observations.

### Tools Used

**Calculator Tool**

Performs arithmetic calculations such as addition, subtraction, multiplication, and division.

**Search Tool**

Retrieves information from a small predefined knowledge base.

The search tool in this experiment is a local demonstration, not a live internet search engine.

## Algorithm

1. Start the program.
2. Import the required libraries.
3. Configure the Large Language Model.
4. Define a calculator tool.
5. Define a search tool.
6. Register the tools with the agent.
7. Accept a user query.
8. Allow the agent to select an appropriate tool.
9. Execute the tool and collect its observation.
10. Repeat tool execution if necessary.
11. Generate and display the final answer.
12. Stop the program.

## Technologies Used

- Python 3
- LangChain
- OpenAI API
- ReAct Agent Architecture
- Calculator Tool
- Local Search Tool

## Requirements

Install the required packages:

```bash
pip install langchain langchain-openai python-dotenv
```

Create a `.env` file in the repository root:

```text
OPENAI_API_KEY=your_api_key_here
```

Never upload your actual API key to GitHub.

## How to Run

```bash
python main.py
```

## Expected Result

The agent accepts user queries and selects suitable tools.

Example 1:

Question: What is 25 multiplied by 4?

Tool: Calculator

Result: 100

Example 2:

Question: What is Agentic AI?

Tool: Search

Result: Agentic AI refers to AI systems that pursue goals through planning, decision-making, and actions.

## Advantages

1. Supports tool-based problem-solving.
2. Combines reasoning with actions.
3. Enables multi-step task execution.
4. Extends LLM capabilities through external tools.
5. Produces answers using tool observations.

## Applications

- AI Personal Assistants
- Automated Research Assistants
- Mathematical Problem Solvers
- Customer Support Agents
- Task Automation Systems

## Conclusion

This experiment demonstrates a ReAct-style intelligent agent using LangChain and tool calling.

The agent selects tools, observes their results, and generates answers to user queries.

The implementation uses a simplified tool-calling agent loop to demonstrate ReAct principles.
