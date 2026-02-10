""" 
    Title: Kueneke_lemonadeStandSchedule.py
    Author: Shannon Kueneke
    Date: Feb 10, 2026
    Description: Hands-On 3.1: Conditionals, Lists, and Loops
"""

#defining lemonade stand tasks
tasks = ["buy ingredients", "make lemonade", "set up stand", "sell lemonade", "cleaning"]

#print tasks to console
for task in tasks:
    print(task)

#defining days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#print a task for each day of the week with Sat/Sun being rest days
taskIndex = 0

for day in days:
  if day == "Saturday" or day == "Sunday":
    print(day + ": day off for rest")
  else:
    print(day + ": " + tasks[taskIndex])
    taskIndex+=1