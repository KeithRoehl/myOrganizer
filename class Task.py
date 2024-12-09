class Task:
    def __init__(self, name, importance, urgency):
        self.name = name
        self.importance = importance
        self.urgency = urgency
        self.priority = (importance + urgency) / 2  # Calculate priority

    def __str__(self):
        return f"Task: {self.name} | Importance: {self.importance} | Urgency: {self.urgency} | Priority: {self.priority:.2f}"

def get_task_input():
    name = input("Enter task name: ")
    importance = int(input("Enter importance (1 to 5): "))
    urgency = int(input("Enter urgency (1 to 5): "))
    return Task(name, importance, urgency)

def main():
    tasks = []
    print("Task Prioritization Assistant")
    while True:
        task = get_task_input()
        tasks.append(task)
        
        more_tasks = input("Would you like to add another task? (y/n): ").strip().lower()
        if more_tasks != 'y':
            break

    # Sort tasks by priority in descending order
    tasks.sort(key=lambda task: task.priority, reverse=True)

    print("\nYour Prioritized Tasks:")
    for task in tasks:
        print(task)

if __name__ == "__main__":
    main()
