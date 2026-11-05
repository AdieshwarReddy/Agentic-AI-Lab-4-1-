
# Experiment 7: LangGraph Workflow
# Multi-Step Problem Solving with Decision Nodes
# Agentic AI Laboratory
# Malla Reddy University

from typing import TypedDict
from langgraph.graph import StateGraph, START, END


# ---------------------------------------
# STEP 1: DEFINE STATE
# ---------------------------------------

class StudentState(TypedDict):
    name: str
    marks: list[int]
    percentage: float
    grade: str
    status: str
    message: str


# ---------------------------------------
# STEP 2: CALCULATE PERCENTAGE NODE
# ---------------------------------------

def calculate_percentage(state: StudentState):

    marks = state["marks"]

    total = sum(marks)
    percentage = total / len(marks)

    print("\nNode 1: Calculate Percentage")
    print("Total Marks:", total)
    print("Percentage:", percentage)

    return {"percentage": percentage}


# ---------------------------------------
# STEP 3: ASSIGN GRADE NODE
# ---------------------------------------

def assign_grade(state: StudentState):

    percentage = state["percentage"]

    if percentage >= 90:
        grade = "A+"

    elif percentage >= 80:
        grade = "A"

    elif percentage >= 70:
        grade = "B"

    elif percentage >= 60:
        grade = "C"

    elif percentage >= 40:
        grade = "D"

    else:
        grade = "F"

    print("\nNode 2: Assign Grade")
    print("Grade:", grade)

    return {"grade": grade}


# ---------------------------------------
# STEP 4: CONDITIONAL DECISION FUNCTION
# ---------------------------------------

def check_result(state: StudentState):

    print("\nDecision Node: Check Result")

    if state["percentage"] >= 40:
        print("Decision: PASS")
        return "pass"

    else:
        print("Decision: FAIL")
        return "fail"


# ---------------------------------------
# STEP 5: PASS NODE
# ---------------------------------------

def pass_node(state: StudentState):

    print("\nNode 3: Pass Node")

    message = (
        f"Congratulations {state['name']}! "
        "You have successfully passed."
    )

    return {
        "status": "PASS",
        "message": message
    }


# ---------------------------------------
# STEP 6: FAIL NODE
# ---------------------------------------

def fail_node(state: StudentState):

    print("\nNode 3: Fail Node")

    message = (
        f"Sorry {state['name']}. "
        "You need to improve your performance."
    )

    return {
        "status": "FAIL",
        "message": message
    }


# ---------------------------------------
# STEP 7: CREATE STATEGRAPH
# ---------------------------------------

workflow = StateGraph(StudentState)


# ---------------------------------------
# STEP 8: ADD NODES
# ---------------------------------------

workflow.add_node(
    "calculate_percentage",
    calculate_percentage
)

workflow.add_node(
    "assign_grade",
    assign_grade
)

workflow.add_node(
    "pass_node",
    pass_node
)

workflow.add_node(
    "fail_node",
    fail_node
)


# ---------------------------------------
# STEP 9: ADD EDGES
# ---------------------------------------

workflow.add_edge(
    START,
    "calculate_percentage"
)

workflow.add_edge(
    "calculate_percentage",
    "assign_grade"
)


# ---------------------------------------
# STEP 10: ADD CONDITIONAL EDGES
# ---------------------------------------

workflow.add_conditional_edges(
    "assign_grade",
    check_result,
    {
        "pass": "pass_node",
        "fail": "fail_node"
    }
)

workflow.add_edge("pass_node", END)
workflow.add_edge("fail_node", END)


# ---------------------------------------
# STEP 11: COMPILE GRAPH
# ---------------------------------------

app = workflow.compile()


# ---------------------------------------
# STEP 12: EXECUTE WORKFLOW
# ---------------------------------------

print("EXPERIMENT 7: LANGGRAPH WORKFLOW")
print("=" * 40)

student_name = "Santhosh"

student_marks = [85, 90, 78, 88, 92]

initial_state = {
    "name": student_name,
    "marks": student_marks,
    "percentage": 0.0,
    "grade": "",
    "status": "",
    "message": ""
}

result = app.invoke(initial_state)


# ---------------------------------------
# STEP 13: DISPLAY FINAL RESULT
# ---------------------------------------

print("\n" + "=" * 40)
print("FINAL STUDENT EVALUATION")
print("=" * 40)

print("Student Name:", result["name"])
print("Marks:", result["marks"])
print("Total Marks:", sum(result["marks"]))
print("Percentage:", result["percentage"])
print("Grade:", result["grade"])
print("Status:", result["status"])
print("Message:", result["message"])

print("\nExperiment completed successfully.")
