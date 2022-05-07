import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from addVehicle import *


# create tkinter window 
root = Tk()

root.title('Car Rental Database 2019')

root.geometry("700x1000")

#note book with tabs for each function of database
car_database = ttk.Notebook(root)
car_database.pack()#inflates database notebook

#add vehicle tab
tab1 = Frame(car_database, width=600, height = 600)
#add customer tab
tab2 = Frame(car_database, width=600, height = 600)
#customer lookup
tab3 = Frame(car_database, width=600, height = 600)
#vehicle lookup tab
tab4 = Frame(car_database, width=600, height = 600)
#book rental tab
tab5 = Frame(car_database, width=700, height = 600)
#return rental tab
tab6 = Frame(car_database, width=600, height = 600)

#inflates tabs
tab1.pack(fill = "both", expand = 1)
tab2.pack(fill = "both", expand = 1)
tab3.pack(fill = "both", expand = 1)
tab4.pack(fill = "both", expand = 1)
tab4.pack(fill = "both", expand = 1)
tab4.pack(fill = "both", expand = 1)


#adds tabs to databse notebook
car_database.add(tab1, text = "Add Vehicle")
car_database.add(tab2, text = "Add Customer")
car_database.add(tab3, text = "Customer Lookup")
car_database.add(tab4, text = "Vehicle Lookup")
car_database.add(tab5, text = "Book Rental")
car_database.add(tab6, text = "Return Rental")

#link to sqlite db file
car_database_connect = sqlite3.connect('rental.db')