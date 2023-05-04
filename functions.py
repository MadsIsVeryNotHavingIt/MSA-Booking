import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()
import hashlib


class database_appointments:

    def create_appointment_table(self):
        '''Admin function for creating an appointments table.'''
        print("\n\nCreate Appointments Table\n")

        try:
            cur.execute('''CREATE TABLE tblAPPOINTMENTS (cus_name, cus_address, cus_phone, staff_number, date_time)''') 
            print("Appointments file created.")
            return

        except sqlite3.OperationalError:
            confirmation = ""
            while confirmation != '1' and confirmation != '2':
            #Validation: while loop repeats until user gives an interpreted response.
                print("An appointments table already exists. Would you like to overwrite it? \n 1. Confirm \n 2. Cancel")
                confirmation = input("Enter:")

                if confirmation == '1':
                    cur.execute('''DROP TABLE tblAPPOINTMENTS''')
                elif confirmation == '2':
                    return
                else:
                    print("Please enter a valid input.")

    def new_appointment(self, staff_number):
        '''Function for creating new appointments.'''

        print("\n\nCreate new appointment\n")
    
        print("Please enter new appointment data.")
        cus_name = input("Customer name: ")
        cus_address = input("Address: ")
        cus_phone = input("Phone: ")
        date_time = input("Date and time (dd/mm/yyyy 00:00): ")

        try:
            cur.execute("INSERT INTO tblAPPOINTMENTS VALUES ((?), (?), (?), (?), (?))", (cus_name, cus_address, cus_phone, staff_number, date_time))
            print("New appointment booked.")
        except sqlite3.OperationalError:
            print("Error: Table not found. Please contact an administrator to create or recover the table.")
        except:
            print("Error")
        


class database_staff:

    #ADMIN FUNCTIONS
    def create_staff_table(self):
        '''Admin function for creating a staff table.'''
        print("\n\nCreate Staff Table\n")

        file_created = False
        confirmation = ""
        while confirmation != '2' or file_created != True :
        #Validation: while loop repeats until user gives an interpreted response.
            
            try:
                cur.execute('''CREATE TABLE tblSTAFF (staff_num, staff_name, staff_pass)''') 
                print("Staff file created.")
                file_created = True
                return

            except sqlite3.OperationalError:
                print("A staff table already exists. Would you like to overwrite it? \n 1. Confirm \n 2. Cancel")
                confirmation = input("Enter:")

                if confirmation == '1':
                    cur.execute('''DROP TABLE tblSTAFF''')
                elif confirmation == '2':
                    return
                else:
                    print("Please enter a valid input.")

            except:
                print("Error")
        


    def new_staff_login(self):
        '''Admin function for creating new staff member logins.'''

        print("\n\nCreate new staff login\n")
    
        print("Please enter new user data.")
        staff_number = input("Please enter your staff number: ")
        staff_name = input("Please enter your name: ")
        staff_password = input("Please enter a password: ").encode

        hashlib_sha1 = hashlib.sha1(staff_password)
        staff_password_hashed = hashlib_sha1.digest()
        #Encodes the staff passwords and returns a hash value


        try:
            cur.execute("INSERT INTO tblSTAFF VALUES ((?), (?), (?))", (staff_number, staff_name, staff_password_hashed))
            print("New login created.")
        except sqlite3.OperationalError:
            print("Error: Table not found. Please contact an administrator to create or recover the table.")
        except:
            print("Error")

class main_functions:

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
            password = input("Password: ").encode().hexdigest()
            password = hashlib.sha1(password)
            try:
                cur.execute("SELECT staff_password FROM tblSTAFF WHERE staff_num = (?)", (staff_number))
                #Uses sqlite3 module to query the database, where the cursor has been defined at the top of the file
                if cur.fetchall() == password:
                    print("Login successful!")
                    main_functions.menu(self, admin = False)
            except sqlite3.OperationalError:
                print("Incorrect login details.")

                tries = tries + 1

    def admin_login(self):
        '''Login for administrators.'''

        print("\n\nAdmin Login\n\n")
        for tries in range(0,3):
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
