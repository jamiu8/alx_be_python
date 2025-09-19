# daily_reminder.py

# Prompt for task details
Task = input("Enter your task: ")
Priority = input("Enter the task's priority (high, medium, low): ").lower()
Time_Bound = input("Is this task time-bound? (yes/no): ").lower()

# Process with match-case
match Priority:
    case "high":
        reminder = f"Your task '{Task}' is HIGH priority. Don't delay!"
    case "medium":
        reminder = f"Your task '{Task}' has a MEDIUM priority. Plan accordingly."
    case "low":
        reminder = f"Your task '{Task}' is LOW priority. Handle it when possible."
    case _:
        reminder = f"Your task '{Task}' has an UNKNOWN priority. Double-check!"

# Add time-sensitive condition
if Time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Final output
print("\n=== Daily Reminder ===")
print(reminder)
