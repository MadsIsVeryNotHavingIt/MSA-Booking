import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()

class menu_navigation():
    def __init__(self):
        ()
    
    def boot_login(self):
        '''Prompts user for next method/function to launch, launches selected method/function'''

        print("Welcome to MSA Bookings.")
        login_or_new = input("Please select an option to continue; \n 1. Login \n 2. Admin Login \n Enter:")
        if login_or_new == '1':
            logged_in = staff_management.tbl_staff_login(self = staff_management, admin = False)
        logged_in = False
        while logged_in != True:
            
            logged_in = staff_management.tbl_staff_login(self = staff_management, admin = True)
        
    def main_menu(self):

        ()
        

class staff_management():
    def __init__(self, database, tables):
        self.database = database
        self.tables = tables

    #def select_option(self):
    #    valid = None
    #    while valid != True:
    #        select = (input("Please login or make a new account;\n 1. Login\n 2. Create staff login \nEnter: "))
    #        try:
    #            select_str = str(select)
    #            print(select_str)
    #            if select_str == '1' or '2':
    #                valid = True
    #        except:
    #            ()
    #        if select_str == '1':
    #            staff_management.tbl_staff_login(self)
    #        elif select_str == '2':
    #            staff_management.tbl_staff_insert(self)
    #        else:
    #            print("\nError. Please enter a valid input\n")
    #            staff_management.select_option(self)
      
    def tbl_staff_login(self, admin):
        print("STAFF LOGIN \nEnter your staff number and password to login;")
        input_num = str(input("Staff Number: "))
        input_pass = hash(str(input("Password: ")))
        cur.execute("SELECT staff_pass FROM tblSTAFF WHERE staff_num LIKE (?)", (input_num))
        staff_pass = cur.fetchall()
        print(staff_pass, input_pass)
        for i in range(0, 2):
            if input_pass == staff_pass:
                print("Login successful.")
                logged_in = True
                return logged_in
            else:
                print("Login unsuccessful.")
                logged_in = False
                return logged_in

    def tbl_staff_create(self):
        cur.execute('''CREATE TABLE tblSTAFF
                 (staff_num, staff_name, staff_pass, staff_email, staff_phone)''')
        print("Staff file created.")

    def tbl_staff_insert(self):
        staff_num, staff_name, staff_pass, staff_email, staff_phone = staff_management.get_staff_data(self)
        try:
            cur.execute("INSERT INTO tblSTAFF VALUES ((?), (?), (?), (?), (?))", (staff_num, staff_name, staff_pass, staff_email, staff_phone))
            print("New login created.")
        except sqlite3.OperationalError:
            staff_management.tbl_staff_create(self = staff_management)
        except:
            print("Error")

    def tbl_staff_read(self, staff_num, staff_name, staff_pass, staff_email, staff_phone):
        ()

    def get_staff_data(self):
        staff_num = str(input('Enter staff number: '))
        staff_name = str(input('Enter name: '))
        staff_pass = str(input('Enter new password: '))
        staff_email = str(input('Enter email: '))
        staff_phone = str(input('Enter phone number: '))
        return (staff_num, staff_name, staff_pass, staff_email, staff_phone)
        
        ######

class apppintments_management():
    def __init__(self, database, tables):
        self.database = database
        self.tables = tables

    def tbl_appointments_create(self):
        cur.execute('''CREATE TABLE tblAPPOINTMENTS
                 (staff_num, customer_num, time_slot_ID)''')
        print("Appointments file created.")

    def tbl_appointments_insert(self):
        staff_num, customer_num, time_slot_ID = apppintments_management.get_appointment_data(self)
        try:
            cur.execute("INSERT INTO tblAPPOINTMENTS VALUES ((?), (?), (?))", (staff_num, customer_num, time_slot_ID))
        except sqlite3.OperationalError:
            print("Appointments file not found.")
        except:
            print("Error.")

    def tbl_appointments_read(self):
        ()   

    def get_appointment_data(self):
        staff_num = ()
        customer_num = ()
        time_slot_ID = ()
        return staff_num, customer_num, time_slot_ID

class time_slots_management():
    def __init__(self, database, tables):
        self.database = database
        self.tables = tables

    def tbl_time_slots_create(self):
        cur.execute('''CREATE TABLE tblTIMETABLE
                    (time_slot_ID, )''')
        print("Timetable file created...")

    def tbl_time_slots_insert(self, staff_num, customer_num):
        time_slot_ID, date_time, used = time_slots_management.get_time_slots(self)
        try:
            cur.execute("INSERT INTO tblAPPOINTMENTS VALUES ((?), (?), (?))", (staff_num, customer_num, time_slot_ID))
        except sqlite3.OperationalError:
            print("Timetable file not found.")
        except:
            print("Error")

    def tbl_time_slots_read(self):
        return

    def get_time_slots(self):
        time_slot_ID = ()
        date_time = ()
        used = ()
        return time_slot_ID, date_time, used


    
