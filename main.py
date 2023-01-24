import sqlite3
con = sqlite3.connect('msaBooking.db')
cur = con.cursor()

from classes import staff_management
from classes import apppintments_management
from classes import time_slots_management
from classes import menu_navigation

### DONE: dynamic sql statements in subroutines, inputting / outputting staff data, 
###MUST DO: Hashing passwords, use staffdata subroutines & database tables for appointments and tiem slots tables, create sequence of steps after boot, 

###BOOT###
menu_navigation.boot_login(self = menu_navigation)

