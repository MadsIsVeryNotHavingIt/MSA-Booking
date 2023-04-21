import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()
import hashlib


class database_appointments():
    def __init__(self):
        ()

    def create_appointment(self):
        '''Book a new appointment.'''

        #tbl_appointments(appointment_ID, customer_name, customer_address, customer_phone, staff_ID)
        


class database_staff():
    def __init__(self):
        ()


    #ADMIN FUNCTIONS
    def create_staff_table(self):
        '''Admin function for creating a staff table.'''
        print("\n\nCreate Staff Table\n")
        confirmation = ""
        while confirmation != '1' and confirmation != '2':
            #Validation: while loop repeats until user gives an interpreted response.
            print("Are you sure you want to create a new staff table? \n 1. Confirm \n 2. Cancel")
            confirmation = input("Enter:")
            if confirmation == '1':
                cur.execute('''CREATE TABLE tblSTAFF (staff_num, staff_name, staff_pass)''') 
                #
                print("Staff file created.")
                return
            elif confirmation == '2':
                return
            else:
                print("Please enter a valid input.")

    def new_staff_login(self):
        '''Admin function for creating new staff member logins.'''

        print("\n\nCreate new staff login\n")
        print("Please enter new user data:")
        staff_number = input("Please enter your staff number: ")
        staff_name = input("Please enter your name: ")
        staff_password = input("Please enter a password: ")

        #Hashing
        hashlib_sha1 = hashlib.sha1(staff_password)
        staff_password_hashed = hashlib_sha1.digest()

        try:
            cur.execute("INSERT INTO tblSTAFF VALUES ((?), (?), (?))", (staff_number, staff_name, staff_password_hashed))
            print("New login created.")
        except sqlite3.OperationalError:
            print("Error: Table not found. Please contact an administrator to create or recover the table.")
        except:
            print("Error")

class main_functions():
    def __init__(self):
        ()

    #def startup(self):
    #    '''user selects a login option.'''
    #
    #    print("Select login option: \n 1. Staff member login \n 2. Administrator login")
    #    login_selection = input("Enter: ")
    #    if login_selection == '1':
    #        main_functions.staff_login(self)
    #    elif login_selection == '2':
    #        main_functions.admin_login(self)
    #        
        #Branches to staff login page or admin login page at the user's choice.
        #Code has been marked as commented and moved to main.py

    def staff_login(self):
        '''Login for regular staff members.'''

        print("\n\nStaff Login\n\n")
        for tries in range(0,2):
            print("Please enter your login details:")
            staff_number = input("Staff number: ")
            password = input("Password: ")
            try:
                cur.execute("SELECT staff_password FROM tblSTAFF WHERE staff_num = (?)", (staff_number))
                #Uses sqlite3 module to query the database, where the cursor has been defined at the top of the file
                if cur.fetchall() == password:
                    print("Login successful!")
                    main_functions.menu(self, admin = False)
            except any:
                print("Incorrect login details.")

                tries = tries + 1

    def admin_login(self):
        '''Login for administrators.'''

        print("\n\nAdmin Login\n\n")
        for tries in range(0,2):
            print("Please enter your login details:")
            staff_number = input("Staff number: ")
            password = input("Password: ")

            if staff_number == 'template_number' and password == 'template_password':
                print("Login successful!")
                menu(admin = True)
            else:
                print("Incorrect login details.")
                tries = tries + 1

        print("Too many attempts! The program will now close.")

    def menu(self, admin):
        pass

    def staff_menu(self):
        print("\n\nWelcome!\n\n")
        pass
