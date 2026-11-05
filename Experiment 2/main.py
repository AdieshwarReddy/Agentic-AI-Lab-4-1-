
# Experiment 2: Traditional AI vs Generative AI vs Agentic AI
# Agentic AI Laboratory

import random

# ---------------------------------------
# 1. TRADITIONAL AI
# ---------------------------------------

def traditional_ai(marks):
    if marks >= 40:
        return "Pass"
    return "Fail"


# ---------------------------------------
# 2. GENERATIVE AI
# Simple Markov Chain Text Generator
# ---------------------------------------

def generative_ai():
    training_text = (
        "AI helps students learn new skills. "
        "AI helps developers build applications. "
        "Students learn new technologies. "
        "Developers build intelligent applications."
    )

    words = training_text.replace(".", "").split()

    transitions = {}

    for current, following in zip(words, words[1:]):
        transitions.setdefault(current, []).append(following)

    random.seed(10)

    current_word = "AI"
    generated = [current_word]

    for _ in range(7):
        next_words = transitions.get(current_word)

        if not next_words:
            break

        current_word = random.choice(next_words)
        generated.append(current_word)

    return " ".join(generated) + "."


# ---------------------------------------
# 3. AGENTIC AI
# Goal-Oriented Task Agent
# ---------------------------------------

def agentic_ai(tasks):
    completed_tasks = []

    while tasks:
        # Select task with highest priority
        task = min(
            tasks,
            key=lambda x: x["priority"]
        )

        print("Agent selected:", task["name"])
        print("Agent executing:", task["name"])

        completed_tasks.append(task["name"])
        tasks.remove(task)

    return completed_tasks


# ---------------------------------------
# MAIN PROGRAM
# ---------------------------------------

print("EXPERIMENT 2: AI COMPARISON")
print("=" * 40)

# Traditional AI
print("\n1. TRADITIONAL AI")

marks = 75
result = traditional_ai(marks)

print("Student Marks:", marks)
print("Prediction:", result)

# Generative AI
print("\n2. GENERATIVE AI")

generated_text = generative_ai()

print("Generated Text:", generated_text)

# Agentic AI
print("\n3. AGENTIC AI")

tasks = [
    {"name": "Read Notes", "priority": 3},
    {"name": "Prepare for Exam", "priority": 1},
    {"name": "Complete Assignment", "priority": 2}
]

completed = agentic_ai(tasks)

print("\nCompleted Tasks:")
for task in completed:
    print("-", task)

print("\nAll demonstrations completed successfully.")
