# Lesson 3.2: Use Functions
# Mini-Project: Take a Break

# Write a program that prompts the user to take a break
# once every two hours, a maximum of three times.

# Use this space to describe your approach to the problem.
#open browser
#time delay
#repetition fo 3 times a day
#

# Your code here.

import time
import webbrowser


print("Take a Break",time.ctime())
for i in range(0,3):
    
    time.sleep(2*60*60)# delay for 2 hours
    print("Time to take a break"time.ctime())
    webbrowser.open("https://www.youtube.com/watch?v=mk48xRzuNvA") # Hall of the fame song link on youtube.

