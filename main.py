import sqlite3
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

    print("\n\nStaff Login\n")
    for tries in range(0,2):
        print("Please enter your login details:")
        staff_number = input("Staff number: ")
        password = input("Password: ")
        try:
            cur.execute("SELECT staff_password FROM tblSTAFF WHERE staff_num = (?)", (staff_number))#
            if cur.fetchall() == password:
                print("Login successful!")
                menu(admin = False)
        except:
            print("Incorrect login details.")
            tries = tries + 1

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
            menu(admin = True)
        
        else:
            print("Incorrect login details.")
            tries = tries + 1
    if tries >= 3:
        print("Too many attempts!")
    print("The program will now close.")



def menu(admin):
    ()


import hashlib

#Hashing
staff_password = ""

hashlib_sha1 = hashlib.sha1(staff_password)
staff_password_hashed = hashlib_sha1.digest()