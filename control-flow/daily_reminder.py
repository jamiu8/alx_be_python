# daily_reminder.py

# Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process with match-case
match priority:
    case "high":
        reminder = f"Your task '{task}' is HIGH priority. Don't delay!"
    case "medium":
        reminder = f"Your task '{task}' has a MEDIUM priority. Plan accordingly."
    case "low":
        reminder = f"Your task '{task}' is LOW priority. Handle it when possible."
    case _:
        reminder = f"Your task '{task}' has an UNKNOWN priority. Double-check!"

# Add time-sensitive condition
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"

# Final output
print(f"Reminder: {reminder}")
