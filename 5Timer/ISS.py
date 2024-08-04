from datetime import datetime
import matplotlib.pyplot as plt

def break_the_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    # personal details
    goal = 60
    hourly_wage = 30  # euros

    # total time elapsed in seconds
    time_elapsed = (datetime.now() - start_date).total_seconds()

    # Calculate the cost and time wasted
    cost = cost_per_day * (time_elapsed / 1440)  # Assuming 14400 minutes in a day
    time_wasted = minutes_wasted * (time_elapsed / 60)

    print(f"Current time: {datetime.now()}")
    print(f"Total time elapsed: {time_elapsed:.2f} seconds")
    print(f"Total cost: {cost:.2f} euros")
    print(f"Total time wasted: {time_wasted:.2f} minutes")

    # Create a simple bar plot
    labels = ['Cost', 'Time without Acting']
    values = [cost, time_wasted]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, values)
    ax.set_title(f"Breaking the '{habit_name}' Habit")
    ax.set_xlabel("Metric")
    ax.set_ylabel("Value")
    plt.show()

# Example usage
start_date = datetime(2024, 7, 13, 10, 0, 0)
break_the_habit("Cleaning the modules", start_date, 1.0, 15)
break_the_habit("IROSA maintenance", start_date, 15, 1)
break_the_habit("Team Social Interactions", start_date, 5.0, 45) 
break_the_habit("Cut the Hair", start_date, 1.0, 15)
break_the_habit("Check the Spacesuits", start_date, 15, 1)

