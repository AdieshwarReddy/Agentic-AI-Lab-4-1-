
# Experiment 1: Rule-Based Intelligent Agent
# Agentic AI Laboratory

tasks = [
    {"name": "Complete Assignment", "priority": 2, "deadline": 3},
    {"name": "Prepare for Exam", "priority": 1, "deadline": 1},
    {"name": "Submit Project", "priority": 1, "deadline": 2},
    {"name": "Read Notes", "priority": 3, "deadline": 4}
]

def schedule_tasks(tasks):
    return sorted(
        tasks,
        key=lambda task: (task["priority"], task["deadline"])
    )

scheduled_tasks = schedule_tasks(tasks)

print("RULE-BASED INTELLIGENT AGENT")
print("----------------------------")

for i, task in enumerate(scheduled_tasks, 1):
    print(
        f"{i}. {task['name']} | "
        f"Priority: {task['priority']} | "
        f"Deadline: {task['deadline']} days"
    )

print("\nTask scheduling completed successfully.")
