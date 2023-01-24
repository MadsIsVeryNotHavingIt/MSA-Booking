import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()

from classes import staff_management
from classes import apppintments_management
from classes import time_slots_management
from classes import menu_navigation

### DONE: dynamic sql statements in subroutines, inputting / outputting staff data, subroutines for each table
###MUST DO: Hashing passwords, create sequence of steps after boot, use date time data type for tbl_TIMETABLE

###BOOT###
menu_navigation.boot_login(self = menu_navigation)

