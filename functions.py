import sqlite3
import sys
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()
import hashlib


class database_appointments:

    def create_appointment_table(self):
        '''Admin function for creating an appointments table.'''
        print("\n\nCreate Appointments Table\n")
        
        file_created = False
        confirmation = ""
        while confirmation != '2' or file_created is not True :
        #Validation: while loop repeats until user gives an interpreted response.
            
            try:
                cur.execute('''CREATE TABLE tblAPPOINTMENTS (cus_name, cus_address, cus_phone, staff_number, date_time)''') 
                print("Appointments file created.")
                file_created = True
                return

            except sqlite3.OperationalError:
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

    def view_appointment(self):
        print("\n\nView Appointments. \n")
        


class database_staff:

    #ADMIN FUNCTIONS
    def create_staff_table(self):
        '''Admin function for creating a staff table.'''
        print("\n\nCreate Staff Table\n")

        file_created = False
        confirmation = ""
        while confirmation != '2' or file_created is not True :
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


