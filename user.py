import tkinter as tk
from tkinter import messagebox

#User Information
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.habits = []

    def add_habit(self, habit):
        self.habits.append(habit)

    def remove_habit(self, habit_id: int):
        self.habits = [habit for habit in self.habits if habit.habit_id != habit_id]

    def get_habits(self) -> List['Habit']:
        return self.habits

class Habit:
    def __init__(self, habit_id: int, name: str, description: str, frequency: str):
        self.habit_id = habit_id
        self.name = name
        self.description = description
        self.frequency = frequency
        self.logs = []

    def add_log_entry(self, log_entry):
        self.logs.append(log_entry)

    def remove_log_entry(self, log_id: int):
        self.logs = [log for log in self.logs if log.log_id != log_id]

    def get_log_entries(self) -> List['LogEntry']:
        return self.logs

class LogEntry:
    def __init__(self, log_id: int, date: datetime, status: str):
        self.log_id = log_id
        self.date = date
        self.status = status

    def update_status(self, new_status: str):
        self.status = new_status

#--------------------------------------------------------------------------------

