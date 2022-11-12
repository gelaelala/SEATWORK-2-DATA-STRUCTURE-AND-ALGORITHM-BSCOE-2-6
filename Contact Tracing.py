# Seatwork 2
# - write a python program for contact tracing
# key: full name
# value: another dictionary of personal information

# import modules (colored for colored text, timer for when the next text to appear, datetime for the current date and time when the contact tracing form was generated)
import colored
from colored import stylize
import time 
from datetime import datetime

# write program intro
def intro():
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
def program_menu ():
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
    print ()

# ask user input and create option 1: add items
def options ():
    contact_tracing  = {}
    while True:
        user_input = int(input("               Which from the option do you want to do (1-3)? "))
        print ()
        if user_input == 1:
            header_info = "══════════════════════════════ ADDING INFORMATION ═════════════════════════════════════"
            print (stylize (header_info, colored.fg ('wheat_1')))
            print (stylize("    * Please add all the necessary information being asked. If none, write N/A. *", colored.fg ('gold_1')))
            print ()
            time.sleep(1)
            full_name = input (stylize ("Please type your full name here (LAST NAME, FIRST NAME, MIDDLE INITIAL): ", colored.fg ('wheat_1'))).title()
            age = input (stylize ("Enter age here: ", colored.fg ('wheat_1')))
            sex = input (stylize ("Enter sex here (MALE/FEMALE): ", colored.fg ('wheat_1'))).upper()
            birthday = input (stylize ("Enter your birthday here (MM/DD/YYYY): ", colored.fg ('wheat_1')))
            address = input (stylize ("Enter your full address here: ", colored.fg ('wheat_1'))).title()
            phone_number = input (stylize ("Enter your phone number here: ", colored.fg('wheat_1')))
            email = input (stylize ("Enter your email address here: ", colored.fg ('wheat_1')))
            first_vac = input (stylize ("Enter the date of your first vaccination here (MM/DD/YYYY): ", colored.fg('wheat_1')))
            first_vac_brand = input (stylize ("Enter the brand of vaccination for first dose: ", colored.fg ('wheat_1'))).title()
            second_vac = input (stylize ("Enter the date of your second vaccination here (MM/DD/YYYY): ", colored.fg ('wheat_1')))
            second_vac_brand = input (stylize ("Enter the brand of vaccination for second dose: ", colored.fg ('wheat_1'))).title()
            booster = input (stylize ("Had booster shot (yes/no): ", colored.fg ('wheat_1'))).upper()
            print ()
            time.sleep (1)
            print (stylize ("* For booster shot details, if YES, please indicate details below. If NO, please write N/A for the following details. *", colored.fg('gold_1')))
            print ()
            time.sleep (1)
            booster_date = input (stylize ("Enter the date of your booster shot here (MM/DD/YYYY): ", colored.fg('wheat_1')))
            booster_vac_brand = input (stylize ("Enter the brand of vaccination for booster shot: ", colored.fg ('wheat_1'))).title()
            print ()
            time.sleep (3)
            print (stylize (f"* NOTICE: DETAILS FOR {full_name.upper()} HAS BEEN SAVED! *", colored.fg('gold_1')))
            print (stylize (f"* A total of {len(contact_tracing) + 1} person/s saved on the contact list *", colored.fg('gold_1')))
            time.sleep (1)
            print ()
            print (stylize ("═" * len(header_info), colored.fg ('wheat_1')))
            print ()
            time.sleep (1)
            contact_tracing[full_name] = {
                "Fullname": full_name,
                "Age": f"{age} years old",
                "Sex": sex,
                "Birthday": birthday,
                "Address": address,
                "Phone Number": phone_number,
                "Email Address": email,
                "First Vaccination Date": first_vac,
                "Brand of First Vaccination": first_vac_brand,
                "Second Vaccination Date": second_vac,
                "Brand of Second Vaccination": second_vac_brand,
                "Booster Shot": booster,
                "Booster Shot Date": booster_date,
                "Brand of Booster Shot": booster_vac_brand
            }
        elif user_input == 2: # create option 2: search for item (full name)
            header_search = "════════════════════════════════ SEARCH FOR INFO ══════════════════════════════════════"
            print (stylize (header_search, colored.fg ('sky_blue_3')))
            print ()
            name_input = input(stylize("Pleasr type the name of the person here (LAST NAME, FIRST NAME, MIDDLE INITIAL): ", colored.fg('sky_blue_3'))).title()
            print ()
            time.sleep (2)
            if name_input in contact_tracing:
                print (stylize ("Name has been found. Generating the form.", colored.fg ('pale_green_3b')))
                print ()
                time.sleep (2)
                print ()
                date_time = datetime.now()
                date = date_time.strftime("%B %d, %Y")
                time_now = date_time.strftime("%I:%M %p")
                header_form = f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ CONTACT TRACING DETAILS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
                print (stylize (header_form, colored.fg ('steel_blue_3')))
                print ()
                time.sleep (1)
                print (stylize ("                               PERSONAL INFORMATION", colored.fg('orange_1')))
                print ()
                print ("Name: ", contact_tracing[name_input]["Fullname"])
                print ("Age: ", contact_tracing[name_input]["Age"])
                print ("Sex: ", contact_tracing[name_input]["Sex"])
                print ("Birthday: ", contact_tracing[name_input]["Birthday"])
                print ("Address: ", contact_tracing[name_input]["Address"])
                print ("Phone Number: ", contact_tracing[name_input]["Phone Number"])
                print ("Email Address: ", contact_tracing[name_input]["Email Address"])
                print ()
                print (stylize (f"               VACCINATION DETAILS (as of {date}, {time_now})", colored.fg('orange_1')))
                print ()
                print ("Date of First Dose: ", contact_tracing[name_input]["First Vaccination Date"])
                print ("Brand of First Dose: ", contact_tracing[name_input]["Brand of First Vaccination"])
                print ("Date of Second Dose: ", contact_tracing[name_input]["Second Vaccination Date"])
                print ("Brand of Second Dose: ", contact_tracing[name_input]["Brand of Second Vaccination"])
                print ("Had taken booster shot: ", contact_tracing[name_input]["Booster Shot"])
                print ("Date of Booster Shot: ", contact_tracing[name_input]["Booster Shot Date"])
                print ("Brand of Booster Shot: ", contact_tracing[name_input]["Brand of Booster Shot"])
                print ()
                time.sleep (1)
                print (stylize("━" * len(header_form), colored.fg('steel_blue_3')))
                print()
                time.sleep (1)
                print (stylize ("═" * len(header_search), colored.fg('sky_blue_3')))
                print()
                time.sleep(1)
            else:
                print (stylize (f"Sorry, the name you have entered ({name_input}) is not registered in our list of contact tracing details. Please try again.", colored.fg('red_1')))
                print ()
                time.sleep(1)
                print (stylize ("═" * len(header_search), colored.fg('sky_blue_3')))
                print ()
                time.sleep (1)
        elif user_input == 3: # create option 3: exit program
            header_exit = "═════════════════════════════════ EXIT PROGRAM ════════════════════════════════════════"
            print (stylize (header_exit, colored.fg('light_pink_1')))
            print ()
            time.sleep(1)
            exit_ques = input("                 Do you want to exit the program (yes/no): ").upper()
            print ()
            time.sleep (1)
            if exit_ques == 'YES':
                print (stylize ("   Program will close at any moment. Thank you for using our contact tracing program.", colored.fg ('red_1')))
                print ()
                time.sleep (1)
                print (stylize ("═" * len(header_exit), colored.fg('light_pink_1')))
                break
            else: 
                print (stylize ("             Program will continue as said so. Please wait a little.", colored.fg ('light_green_3')))
                print ()
                time.sleep (1)
                print (stylize ("═" * len(header_exit), colored.fg('light_pink_1')))
                print ()
                time.sleep (1)

def main ():
    intro ()
    program_menu ()
    options ()

main ()