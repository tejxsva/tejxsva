import json
import os
from datetime import date

HABITS_FILE = "habits.json"

def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "r") as f:
            return json.load(f)
    else:
        return {}

def save_habits(habits):
    with open(HABITS_FILE, "w") as f:
        json.dump(habits, f, indent=2)

def add_habit(habits, habit_name):
    if habit_name not in habits:
        habits[habit_name] = []
        print(f"Habit '{habit_name}' added.")
    else:
        print(f"Habit '{habit_name}' already exists.")

def mark_habit(habits, habit_name):
    today = str(date.today())
    if habit_name in habits:
        if today not in habits[habit_name]:
            habits[habit_name].append(today)
            print(f"Habit '{habit_name}' marked as done for today.")
        else:
            print(f"Habit '{habit_name}' already marked as done today.")
    else:
        print(f"Habit '{habit_name}' does not exist.")

def view_habits(habits):
    for habit, dates in habits.items():
        print(f"{habit}: {len(dates)} days tracked")

def main():
    habits = load_habits()
    while True:
        print("\nHabit Tracker")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            habit_name = input("Enter habit name: ")
            add_habit(habits, habit_name)
            save_habits(habits)
        elif choice == "2":
            habit_name = input("Enter habit name: ")
            mark_habit(habits, habit_name)
            save_habits(habits)
        elif choice == "3":
            view_habits(habits)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
