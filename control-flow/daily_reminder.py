task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case priority = "high":
        reminder = f"'{task}' is a high priority task"
    case priority = "medium":
        reminder = f"'{task}' is a medium priority task"
    case priority = "low":
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"Invalid priority input."
if time_bound == "yes":
    reminder += "that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."
print(f"Reminder: {reminder}")

