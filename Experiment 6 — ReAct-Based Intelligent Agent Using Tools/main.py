
# Experiment 6: ReAct-Based Intelligent Agent
# Agentic AI Laboratory
# Malla Reddy University

import os
import ast
import operator

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage
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
# STEP 2: DEFINE CALCULATOR TOOL
# ---------------------------------------

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv
}


def evaluate_expression(node):

    if isinstance(node, ast.Expression):
        return evaluate_expression(node.body)

    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float):
            return node.value

    if isinstance(node, ast.UnaryOp):
        value = evaluate_expression(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        if isinstance(node.op, ast.UAdd):
            return value

    if isinstance(node, ast.BinOp):
        operation = OPERATORS.get(type(node.op))

        if operation is not None:
            left = evaluate_expression(node.left)
            right = evaluate_expression(node.right)

            return operation(left, right)

    raise ValueError("Unsupported expression")


@tool
def calculator(expression: str) -> str:
    """Calculate a basic arithmetic expression."""

    try:
        if len(expression) > 100:
            return "Error: Expression too long"

        tree = ast.parse(expression, mode="eval")
        result = evaluate_expression(tree)

        if abs(result) > 1e15:
            return "Error: Result too large"

        return str(result)

    except (ValueError, SyntaxError,
            ZeroDivisionError, OverflowError,
            RecursionError) as error:
        return f"Calculation error: {error}"


# ---------------------------------------
# STEP 3: DEFINE SEARCH TOOL
# ---------------------------------------

@tool
def search(query: str) -> str:
    """Search a small local AI knowledge base."""

    knowledge_base = {
        "agentic ai":
            "Agentic AI refers to AI systems that "
            "pursue goals through planning, "
            "decision-making, and actions.",

        "langchain":
            "LangChain is a framework for "
            "building applications powered "
            "by Large Language Models.",

        "react":
            "ReAct combines reasoning and "
            "acting through tool usage "
            "and observations.",

        "python":
            "Python is a high-level "
            "programming language widely "
            "used in AI and machine learning."
    }

    query = query.lower().strip()

    for keyword, answer in knowledge_base.items():
        if keyword in query:
            return answer

    return "No matching information found."


# ---------------------------------------
# STEP 4: INITIALIZE THE LLM
# ---------------------------------------

llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0,
    api_key=api_key
)


# ---------------------------------------
# STEP 5: REGISTER TOOLS
# ---------------------------------------

tools = [calculator, search]

tool_map = {
    tool_item.name: tool_item
    for tool_item in tools
}

agent = llm.bind_tools(tools)


# ---------------------------------------
# STEP 6: REACT AGENT LOOP
# ---------------------------------------

def run_agent(question):

    messages = [
        SystemMessage(
            content=(
                "You are a helpful ReAct-style AI agent. "
                "Use calculator for arithmetic questions "
                "and search for questions about AI topics "
                "available in the local knowledge base. "
                "Use tool results to produce accurate answers."
            )
        ),
        HumanMessage(content=question)
    ]

    # Limit the number of tool-use rounds
    for step in range(5):

        response = agent.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            print("\nFinal Answer:")
            print(response.content)
            return

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print("\nAction:", tool_name)
            print("Action Input:", tool_args)

            selected_tool = tool_map.get(tool_name)

            if selected_tool is None:
                result = "Unknown tool requested."
            else:
                try:
                    result = selected_tool.invoke(tool_args)
                except Exception as error:
                    result = f"Tool error: {error}"

            print("Observation:", result)

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )

    print("\nAgent stopped: Maximum steps reached.")


# ---------------------------------------
# STEP 7: MAIN PROGRAM
# ---------------------------------------

print("EXPERIMENT 6: REACT-BASED AI AGENT")
print("=" * 40)

question = input("\nEnter your question: ").strip()

if not question:
    print("Please enter a valid question.")

else:
    try:
        run_agent(question)
        print("\nExperiment execution finished.")

    except Exception as error:
        print("\nError:", error)
        print("Check your API key and connection.")
