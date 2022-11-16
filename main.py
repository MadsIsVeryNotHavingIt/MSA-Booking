import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()

# Create table
def tblStaffCreate():
  cur.execute('''CREATE TABLE staffList
                  (staffNum, staffName, staffPass, staffEmail, staffPhone)''')

from os import path
print('MSABooking: ', path.exists('msaBooking.db'))
if (path.exists('msaBooking.db')) != True:

  tblStaffCreate()
  print("No file detected. Creating file...")


# Create table
def tblStaffCreate():
  cur.execute('''CREATE TABLE staffList
                 (staffNum, staffName, staffPass, staffEmail, staffPhone)''')
  print("Staff file created...")
  insertStaffDetails

# Insert a row of data
def insertStaffDetails(staffNum, staffName, staffPass, staffEmail, staffPhone):
  cur.execute("INSERT INTO staffList VALUES (?, ?, ?, ?, ?)", (staffNum, staffName, staffPass, staffEmail, staffPhone))


staffNum = str(input('Enter staff number: '))
staffName = str(input('Enter name: '))
staffPass = str(input('Enter new password: '))
staffEmail = str(input('Enter email: '))
staffPhone = str(input('Enter phone number: '))

insertStaffDetails(staffNum, staffName, staffPass, staffEmail, staffPhone)

def displayAllStaff():
  cur.execute("SELECT staffNum, staffName FROM staffList")
  print(cur.fetchall())

con.commit()
con.close()
