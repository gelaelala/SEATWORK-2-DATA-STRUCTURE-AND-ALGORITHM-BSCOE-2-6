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

# ask user input and create option 1: add items
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
        sex = input (stylize ("Enter sex here: ", colored.fg ('wheat_1')))
        birthday = input (stylize ("Enter your birthday here (MM/DD/YYYY): ", colored.fg ('wheat_1')))
        phone_number = input (stylize ("Enter your phone number here: ", colored.fg('wheat_1')))
        email = input (stylize ("Enter your email address here: ", colored.fg ('wheat_1')))
        first_vac = input (stylize ("Enter the date of your first vaccination here (MM/DD/YYYY): ", colored.fg('wheat_1')))
        first_vac_brand = input (stylize ("Enter the brand of vaccination for first dose: ", colored.fg ('wheat_1')))
        second_vac = input (stylize ("Enter the date of your second vaccination here (MM/DD/YYYY): ", colored.fg ('wheat_1')))
        second_vac_brand = input (stylize ("Enter the brand of vaccination for second dose: ", colored.fg ('wheat_1')))
        booster = input (stylize ("Had booster shot (yes/no):", colored.fg ('wheat_1')))
        print ()
        time.sleep (1)
        print (stylize ("* For booster shot details, if YES, please indicate details below. If NO, please write N/A for the following details. *", colored.fg('gold_1')))
        print ()
        time.sleep (1)
        booster_date = input (stylize ("Enter the date of your booster shot here (MM/DD/YYYY): ", colored.fg('wheat_1')))
        booster_vac_brand = input (stylize ("Enter the brand of vaccination for booster shot: ", colored.fg ('wheat_1')))
        contact_tracing[full_name.title()] = {
            f"Fullname: {full_name.title()}",
            f"Age: {age} years old",
            f"Sex: {sex.upper()}",
            f"Birthday: {birthday}",
            f"Phone Number: {phone_number}",
            f"Email Address: {email}",
            f"First Vaccination Date: {first_vac}",
            f"Brand of First Vaccination: {first_vac_brand}",
            f"Second Vaccination Date: {second_vac}",
            f"Brand of Second Vaccination: {second_vac_brand}",
            f"Booster Shot: {booster.upper()}"
            f"Booster Shot Date: {booster_date}",
            f"Brand of Booster Shot: {booster_vac_brand}"
        }

# create option 2: search for item (full name)
# create option 3: exit program