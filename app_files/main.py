import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from addVehicle import *
from addCustomer import *
from listCustomer import *
from listVehicles import *
from bookRental import *
from returnRental import *
from tabs import *


addVehicle()

addCustomer()

listCustomer()

listVehicles()

bookRental()

returnRental()

root.mainloop()
