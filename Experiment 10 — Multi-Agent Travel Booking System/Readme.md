
# Experiment 10: Multi-Agent Travel Booking System

## Aim

To develop a mini multi-agent system for travel booking using Coordinator–Worker–Delegator architecture.

## Objective

To understand how multiple specialized agents collaborate to perform different tasks and achieve a common goal.

## Theory

### What is a Multi-Agent System?

A Multi-Agent System (MAS) consists of multiple agents that interact and collaborate to solve problems.

Each agent performs a specific task, and the results are combined to achieve a common objective.

### Coordinator–Worker–Delegator Architecture

This architecture divides responsibilities among specialized components.

**1. Coordinator Agent**

Receives the user's travel requirements, manages the overall workflow, and combines results.

**2. Delegator Agent**

Assigns specific tasks to suitable worker agents.

**3. Worker Agents**

Perform specialized tasks.

In this experiment, the workers are:

- Flight Agent: Finds available flights.
- Hotel Agent: Finds suitable hotels.
- Budget Agent: Calculates total travel cost.

### Architecture

```text
               User Request
                    |
                    v
             Coordinator Agent
                    |
                    v
              Delegator Agent
                    |
          +---------+---------+
          |         |         |
          v         v         v
       Flight     Hotel     Budget
       Agent      Agent     Agent
          |         |         |
          +---------+---------+
                    |
                    v
             Coordinator Agent
                    |
                    v
             Travel Summary
```

The budget agent receives the selected flight and hotel results before calculating the total cost.

## Problem Statement

Develop a travel booking assistant that:

1. Accepts travel requirements.
2. Searches for flights using a Flight Agent.
3. Searches for hotels using a Hotel Agent.
4. Calculates travel expenses using a Budget Agent.
5. Coordinates agent execution using a Delegator.
6. Generates a final travel summary.

## Algorithm

1. Start the program.
2. Define the travel requirements.
3. Create specialized worker agents.
4. Create a Delegator Agent to assign tasks.
5. Create a Coordinator Agent to manage the workflow.
6. Pass the travel request to the Coordinator.
7. Delegate flight search to the Flight Agent.
8. Delegate hotel search to the Hotel Agent.
9. Delegate budget calculation to the Budget Agent.
10. Combine the results.
11. Display the travel summary.
12. Stop the program.

## Technologies Used

- Python 3
- Object-Oriented Programming
- Multi-Agent Systems
- Coordinator–Worker–Delegator Architecture
- Task Delegation
- Workflow Automation

## Requirements

Python 3.9 or later is recommended.

No external libraries are required.

## How to Run

```bash
python main.py
```

## Expected Result

The system displays:

- Travel destination
- Selected flight
- Selected hotel
- Number of nights
- Flight cost
- Hotel cost
- Total travel cost
- Budget status

## Advantages

1. Modular architecture.
2. Clear separation of responsibilities.
3. Easy integration of additional agents.
4. Reusable agent components.
5. Automated task coordination.
6. Simplified multi-step workflows.

## Limitations

1. Uses predefined travel data.
2. Does not connect to real booking services.
3. Does not make actual reservations.
4. Agents follow programmed rules rather than LLM-based reasoning.
5. Availability and prices are illustrative.

## Applications

- Travel Planning Assistants
- Hotel Recommendation Systems
- Flight Search Systems
- Budget Planning Applications
- Multi-Agent Workflow Automation
- Intelligent Personal Assistants

## Conclusion

This experiment demonstrates a simplified multi-agent travel planning system using Coordinator–Worker–Delegator architecture.

The Coordinator manages the overall task, the Delegator assigns responsibilities, and specialized Worker Agents perform flight selection, hotel selection, and budget calculation.

The system demonstrates task delegation, agent collaboration, and workflow coordination using Python.
