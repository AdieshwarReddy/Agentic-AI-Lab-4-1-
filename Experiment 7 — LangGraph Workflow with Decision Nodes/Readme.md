
# Experiment 7: LangGraph Workflow with Decision Nodes

## Aim

To build a LangGraph workflow for a multi-step problem-solving task using nodes, edges, conditional routing, and state management.

## Objective

To understand how LangGraph can be used to design structured workflows that execute multiple operations and make decisions based on predefined conditions.

## Theory

### What is LangGraph?

LangGraph is a framework for developing stateful workflows and agent-based applications.

It represents application logic as a graph containing nodes and edges.

LangGraph supports sequential execution, conditional branching, cycles, and shared state management.

### Components of LangGraph

**1. State**

State stores information shared between different nodes in the workflow.

**2. Nodes**

Nodes are functions that perform specific tasks such as calculations, evaluations, or data processing.

**3. Edges**

Edges define the connections between nodes and determine the execution flow.

**4. Conditional Edges**

Conditional edges allow the workflow to select different paths based on conditions.

**5. StateGraph**

StateGraph is used to construct workflows that operate on shared state.

## Problem Statement

Develop a Student Performance Evaluation System using LangGraph.

The system should:

1. Accept student marks.
2. Calculate the percentage.
3. Determine the student's grade.
4. Check whether the student passed or failed.
5. Display the final evaluation.

## Workflow Architecture

```text
             START
               |
               v
        Calculate Percentage
               |
               v
          Assign Grade
               |
               v
        Check Pass / Fail
               |
        +------+------+
        |             |
      PASS           FAIL
        |             |
        v             v
   Pass Message   Fail Message
        |             |
        +------+------+
               |
               v
              END
```

## Algorithm

1. Start the program.
2. Import LangGraph and required Python libraries.
3. Define a shared state structure.
4. Create a node to calculate the percentage.
5. Create a node to assign the grade.
6. Create a conditional function to check pass/fail status.
7. Create separate nodes for pass and fail messages.
8. Define nodes and edges using StateGraph.
9. Compile the workflow.
10. Provide student marks as input.
11. Execute the graph.
12. Display the final result.
13. Stop the program.

## Technologies Used

- Python 3
- LangGraph
- StateGraph
- TypedDict
- Conditional Edges
- State Management

## Requirements

Install LangGraph:

```bash
pip install langgraph
```

## How to Run

```bash
python main.py
```

## Expected Result

The workflow evaluates student marks and produces a result containing:

- Student Name
- Total Marks
- Percentage
- Grade
- Pass/Fail Status
- Final Message

## Advantages

1. Supports modular workflow design.
2. Enables conditional decision-making.
3. Maintains shared state between nodes.
4. Supports sequential and branching workflows.
5. Simplifies multi-step application development.

## Applications

- Student Performance Evaluation
- Automated Approval Systems
- AI Workflow Automation
- Customer Support Routing
- Task Planning Systems
- Decision Support Systems

## Conclusion

This experiment demonstrates how LangGraph can be used to implement a multi-step workflow with conditional decision nodes.

The system calculates student performance, assigns a grade, and selects the appropriate result path.

It illustrates graph-based workflow execution and state management without requiring an external LLM.
