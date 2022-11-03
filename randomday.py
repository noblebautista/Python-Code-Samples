# Program Name: randomday.py
# Noble Bautista
# November 3rd, 2022
# CSS-225
# Description: Use random.choice to select a day of the week from a list
# and print that day.

import random # makes sure random is referenced

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# (above) list of days of the week in list (days is declared the variable)
print(random.choice(days))
# (above) prints random day for each time run (from list)
