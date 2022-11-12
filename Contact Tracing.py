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
contact_tracing  = {}
while True:
    user_input = input("Which from the option do you want to do? (1-3) ")
    print ()
    if user_input == '1':
        print (stylize ("══════════════════════════════ ADDING INFORMATION ═════════════════════════════════════", colored.fg ('wheat_1')))
        print (stylize("    * Please add all the necessary information being asked. If none, write N/A. *", colored.fg ('gold_1')))
        print ()
        time.sleep(1)
        full_name = input (stylize ("Please type your full name here (LAST NAME, FIRST NAME, MIDDLE INITIAL): ", colored.fg ('wheat_1')))
        age = input (stylize ("Enter age here: ", colored.fg ('wheat_1')))
        contact_tracing[full_name] = {
            f"Fullname: {full_name.title()}",
            f"Age: {age} years old"
        }
        print (contact_tracing)
# create option 1: add items
# create option 2: search for item (full name)
# create option 3: exit program