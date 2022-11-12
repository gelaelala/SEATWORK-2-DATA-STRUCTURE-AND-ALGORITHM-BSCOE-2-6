# Seatwork 2
# - write a python program for contact tracing
# key: full name
# value: another dictionary of personal information

# import modules (colored for colored text, timer for when the next text to appear)
import colored
from colored import stylize
import time 

# write program intro
print (stylize("══════════════════════════════ CONTACT TRACING ════════════════════════════════════════", colored.fg ('indian_red_1a')))
print ()
time.sleep (1)
print ("A menu will appear where you can choose to add your information and search for it after.")
print ("For the details needed for contact tracing, please input all the information being asked.")
print ()
print (stylize("═══════════════════════════════════════════════════════════════════════════════════════", colored.fg ('indian_red_1a')))
print ()
print ()

# display menu

# ask user input
# create option 1: add items
# create option 2: search for item (full name)
# create option 3: exit program