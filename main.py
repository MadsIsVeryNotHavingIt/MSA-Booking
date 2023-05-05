import sqlite3
import hashlib
import sys
from flask import Flask, render_template, request

con = sqlite3.connect('msaBooking.db')
cur = con.cursor()

from functions import database_appointments, database_staff

def startup():
    '''user selects a login option.'''

    print("Select login option: \n 1. Staff member login \n 2. Administrator login")
    login_selection = input("Enter: ")
    if login_selection == '1':
        staff_login()
    elif login_selection == '2':
        admin_login()
        
   #Branches to staff login page or admin login page at the user's choice.


def staff_login():
    '''Login for regular staff members.'''

    print("\nStaff Login")
    
    forced_login = True    
    for tries in range(0,3):
        print("\nPlease enter your login details:")
        staff_number = input("Staff number: ")
        password = input("Password: ")
        try:
            #cur.execute("SELECT staff_password FROM tblSTAFF WHERE staff_num = (?)", (staff_number))
            #fetches the staff password from the database via searching by staff number
            if cur.fetchall() == password or forced_login == True:
                print("Login successful!")
                menu(admin = False, staff_number = staff_number)
        except:
            print("Incorrect login details.")
            tries = tries + 1
    print("Too many attempts! The program will now shut down.")
    

def admin_login():
    '''Login for administrators.'''

    tries = 0
    logged_in = False
    print("\n\nAdmin Login\n")
    while tries < 3 and logged_in == False:
        print("Please enter your login details:")
        staff_number = input("Staff number: ")
        password = input("Password: ")

        if staff_number == 'template_number' and password == 'template_password':
            print("Login successful!")
            logged_in = True
            menu(admin = True, staff_number = staff_number)
        
        else:
            print("Incorrect login details.\n")
            tries = tries + 1
    if tries >= 3:
        print("Too many attempts!")
    print("The program will now close.")



def login():
    '''Login for staff members and administrators.'''

    print("\n\nStaff Login\n")
    for tries in range(0,2):
        print("Please enter your login details:")
        staff_number = input("Staff number: ")
        password = input("Password: ")

        if staff_number == 'template_number' and password == 'template_password':
            print("Login successful!")
            logged_in = True
            return staff_number
        
        else:
            try:
                cur.execute("SELECT staff_password FROM tblSTAFF WHERE staff_num = (?)", (staff_number))
                #queries the database by staff number to find a corresponding password
                if cur.fetchall() == password:
                    print("Login successful!")
                    menu(admin = False, staff_number = staff_number)
            except:
                print("Incorrect login details.\n")
                tries = tries + 1


def menu(admin, staff_number):
    '''Main menu for staff members and administrators. Behaviour changes depending on state of 'admin' variable.'''

    print("\nMain Menu\n\n")


    #Database display goes here

    if admin == False:
        user_select = ""
        while user_select != '1' and user_select != '2' and user_select != '3':
        #validation loop until user enters an interpretable input

            print("Please select a page. \n 1. Book new login \n 2. View existing appointment \n 3. Log out")
            user_select = input("Enter: ")
            if user_select == '1':
                print("Launching 'book new apppointment' page.")
                database_appointments.new_appointment(self = "", staff_number = staff_number)
            elif user_select == '2':
                print("Launching 'View existing appointment' page.")
                database_appointments.view_appointment(self = "")
            elif user_select == '3':
                sys.exit("Logging out. The program will now close.")
            else:
                print("Error.")

    #cur.execute('''SELECT ALL cus_name, cus_address, cus_phone, staff_number, date_time FROM tblAPPOINTMENTS ORDER BY date_time DESC''')
    #print(cur.fetchall())

def staff_menu():
    '''Main menu for staff members.'''

    #Appointments display goes here.

    user_select = ""
    while user_select != '1' and user_select != '2' and user_select != '3':
    #validation loop until user enters an interpretable input

        print("Please select a page. \n 1. Book new appointment \n 2. View existing appointment \n 3. Log out")
        user_select = input("Enter: ")
        if user_select == '1':
            print("Launching 'book new apppointment' page.")
            database_appointments.new_appointment(self = "", staff_number = staff_number)
        elif user_select == '2':
            print("Launching 'View existing appointment' page.")
            database_appointments.view_appointment(self = "")
        elif user_select == '3':
            sys.exit("Logging out. The program will now close.")
        else:
            print("Error.")

    #cur.execute('''SELECT ALL cus_name, cus_address, cus_phone, staff_number, date_time FROM tblAPPOINTMENTS ORDER BY date_time DESC''')
    #print(cur.fetchall())

#staff_number = login()
#menu()
#test
staff_number = '000123'
