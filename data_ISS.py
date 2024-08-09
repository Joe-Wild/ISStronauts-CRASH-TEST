from datetime import datetime
import matplotlib.pyplot as plt

def break_the_habit(habit_name, start_date, cost_per_day, minutes_wasted):
    # Calculate the total time elapsed in weeks
    time_elapsed_days = (datetime.now() - start_date).days
    time_elapsed_weeks = time_elapsed_days / 7

    # Calculate the cost and time wasted
    cost = cost_per_day * 7 * time_elapsed_weeks  # Weekly cost
    time_wasted = minutes_wasted * 7 * time_elapsed_weeks  # Weekly time wasted

 # Calculate the total cost and time wasted per DAY
    #cost = cost_per_day * time_elapsed_days  # Total cost based on days elapsed
    #time_wasted = minutes_wasted * time_elapsed_days  # Total time wasted based on days elapsed


    print(f"Current time: {datetime.now()}")
    print(f"Total time elapsed: {time_elapsed_weeks:.2f} weeks")
    print(f"Total cost: {cost:.2f} euros")
    print(f"Total time wasted: {time_wasted:.2f} minutes")


#print(f"Current time: {datetime.now()}")
    #print(f"Total time elapsed: {time_elapsed_days} days")
    #print(f"Total cost: {cost:.2f} euros")
    #print(f"Total time wasted: {time_wasted:.2f} minutes")


    # Create a simple bar plot
    labels = ['Cost (Euros)', 'Time Wasted (Minutes)']
    values = [cost, time_wasted]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(labels, values, color=['blue', 'red'])
    ax.set_title(f"Breaking the '{habit_name}' Habit")
    ax.set_xlabel("Metric")
    ax.set_ylabel("Value")
    plt.show()

# Example usage
start_date = datetime(2024, 7, 13, 10, 0, 0)
break_the_habit("Cleaning the modules", start_date, 1.0, 15) #1€/Day
break_the_habit("IROSA maintenance", start_date, 15, 1)
break_the_habit("Team Social Interactions", start_date, 5.0, 45)
break_the_habit("Cut the Hair", start_date, 1.0, 15)
break_the_habit("Check the Spacesuits", start_date, 15, 1)


