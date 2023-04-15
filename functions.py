import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()


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

        cur.execute('''CREATE TABLE tblSTAFF (staff_num, staff_name, staff_pass)''')
        print("Staff file created.")

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
            except:
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
        print("")

    def staff_menu(self):
        print("\n\nWelcome!\n\n")
        print("")
