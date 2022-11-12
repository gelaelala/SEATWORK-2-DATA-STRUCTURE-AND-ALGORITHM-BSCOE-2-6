# Seatwork 2
# - write a python program for contact tracing
# key: full name
# value: another dictionary of personal information

# import modules (colored for colored text, timer for when the next text to appear)
import colored
from colored import stylize
import time 

# write program intro
header = "══════════════════════════════ CONTACT TRACING ════════════════════════════════════════"
print (stylize(header, colored.fg ('indian_red_1a')))
print ()
time.sleep (1)
print ("A menu will appear where you can choose to add your information and search for it after.")
print ("For the details needed for contact tracing, please input all the information being asked.")
print ()
time.sleep (1)
print (stylize("═" * len(header), colored.fg ('indian_red_1a')))
print ()
print ()
time.sleep (1)

# display menu
header_menu = "═════════════════════════════ CONTACT TRACING MENU ════════════════════════════════════"
print (stylize (header_menu, colored.fg ('pale_green_3b')))
print()
time.sleep (1)
print ("               1 --> Add a contact tracing information")
print ("               2 --> Search for person's contact tracing information")
print ("               3 --> Exit program")
print ()
time.sleep (1)
print (stylize ("═" * len(header_menu), colored.fg ('pale_green_3b')))
time.sleep (1)

# ask user input
# create option 1: add items
# create option 2: search for item (full name)
# create option 3: exit program