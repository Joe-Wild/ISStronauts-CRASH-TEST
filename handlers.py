from datetime import datetime, date
from typing import List, Dict

class Habit:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.created_date = date.today()
        self.completed_dates: List[date] = []

    def complete_habit(self, date: date):
        self.completed_dates.append(date)

    def is_habit_completed(self, date: date) -> bool:
        return date in self.completed_dates

class HabitTracker:
    def __init__(self):
        self.habits: List[Habit] = []

    def add_habit(self, habit: Habit):
        self.habits.append(habit)

    def get_habits(self) -> List[Habit]:
        return self.habits

    def get_habit_by_name(self, name: str) -> Habit:
        for habit in self.habits:
            if habit.name.lower() == name.lower():
                return habit
        raise ValueError(f"Habit '{name}' not found.")

    def complete_habit(self, habit_name: str, date: date):
        habit = self.get_habit_by_name(habit_name)
        habit.complete_habit(date)

    def get_completed_habits(self, date: date) -> List[Habit]:
        return [habit for habit in self.habits if habit.is_habit_completed(date)]

    def get_incomplete_habits(self, date: date) -> List[Habit]:
        return [habit for habit in self.habits if not habit.is_habit_completed(date)]

# Example usage
tracker = HabitTracker()

# Add habits
tracker.add_habit(Habit("Exercise", "30 minutes of exercise per day"))
tracker.add_habit(Habit("Language", "30 minutes of speaking English per day"))
tracker.add_habit(Habit("Read", "Read 10 pages per day"))
tracker.add_habit(Habit("FCLvoc", "30 minutes of exercise per day"))
tracker.add_habit(Habit("Guitar", "Play 45 minutes per day"))

# Complete habits
tracker.complete_habit("Exercise", date(2024, 7, 13))
tracker.complete_habit("Language", date(2024, 7, 13))
tracker.complete_habit("Read", date(2024, 7, 13))
tracker.complete_habit("FCLvoc", date(2024, 7, 13))


# Get habit information
print("Completed habits on 2024-07-13:")
for habit in tracker.get_completed_habits(date(2024, 7, 13)):
    print(f"- {habit.name}")

print("\nBroken habits on 2024-07-13:")
for habit in tracker.get_incomplete_habits(date(2024, 7, 13)):
    print(f"- {habit.name}")




