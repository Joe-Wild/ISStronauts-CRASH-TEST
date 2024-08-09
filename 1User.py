import tkinter as tk
from tkinter import messagebox
from typing import List
from datetime import datetime

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

# Example classes with methods to be called by the UI
class FeatureHandler:
    def ask_features(self):
        return "Features: Feature1, Feature2, Feature3"

class ActionHandler:
    def ask_action_done(self):
        return "Actions Done: Action1, Action2"

    def ask_actions_not_done(self):
        return "Actions Not Done: Action3, Action4"

class AnalysisHandler:
    def display_analysis(self):
        return "Analysis: All systems operational."

# Main Application Class
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Feature and Action Analysis")

        # Initialize handlers
        self.feature_handler = FeatureHandler()
        self.action_handler = ActionHandler()
        self.analysis_handler = AnalysisHandler()

        # Create buttons
        self.create_buttons()

    def create_buttons(self):
        tk.Button(self.root, text="Ask Features", command=self.ask_features).pack(pady=5)
        tk.Button(self.root, text="Ask Action Done", command=self.ask_action_done).pack(pady=5)
        tk.Button(self.root, text="Ask Actions Not Done", command=self.ask_actions_not_done).pack(pady=5)
        tk.Button(self.root, text="Display Analysis", command=self.display_analysis).pack(pady=5)

    def ask_features(self):
        features = self.feature_handler.ask_features()
        messagebox.showinfo("Features", features)

    def ask_action_done(self):
        actions_done = self.action_handler.ask_action_done()
        messagebox.showinfo("Actions Done", actions_done)

    def ask_actions_not_done(self):
        actions_not_done = self.action_handler.ask_actions_not_done()
        messagebox.showinfo("Actions Not Done", actions_not_done)

    def display_analysis(self):
        analysis = self.analysis_handler.display_analysis()
        messagebox.showinfo("Analysis", analysis)

# Main function to run the application
def main():
    root = tk.Tk()
    app = App(root)
    root.mainloop()

if __name__ == "__main__":
    main()