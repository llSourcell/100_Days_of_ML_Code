#!/usr/bin/python2

import datetime

now = datetime.datetime.now()

# Get current streak number
with open(".day.dat",'r') as f:
    a = f.readlines()
day = int(a[0])

# Store strings for new bump day
string_day = "### Day " + str(day + 1) + ":\n"
current_date = now.strftime("%d-%m-%Y , %H:%M \n\n")
todays_progress = "**Today's Progress:** " + raw_input("Today's Progress: ") + "\n\n"
thoughts = "**Thoughts:** " + raw_input("Thoughts on Today: ") + "\n\n"

link_url = raw_input("Link URL: ")
link_description = raw_input("Link Description: ")

link_to_work = "**Link to work:** [" + link_description +"](" + link_url + ")\n\n"
footer = "\n***\n"

str_new_day = (string_day + current_date + todays_progress + thoughts + link_to_work + footer)


# Increment current streak number and save on day file
day = day+1
with open(".day.dat",'w') as f:
    f.write(str(day))
    f.close()

# Save string into log file
with open("Log.md", 'a') as log:
    log.write(str_new_day)
