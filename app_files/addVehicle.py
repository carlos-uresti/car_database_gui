import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *




def addVehicle():
   #submit new vehicle info
  def submit():
  	submit_conn = sqlite3.connect('rental.db')
  
  	submit_cur = submit_conn.cursor()
  
  	submit_cur.execute("INSERT INTO VEHICLE VALUES (:VehicleID, :Description, :Year, :Type, :Category) ",
  		{
  			'VehicleID': vehicle_id1.get(),
  			'Description': description.get(),
  			'Year': year1.get(),
  			'Type': type1.get(),
  			'Category': int(category1.get())
  		
  		})
    #commit changes
  	submit_conn.commit()
  	#close the DB connection
  	submit_conn.close() 
  
    
  # input fields 
  vehicle_id1 = Entry(tab1, width = 30)
  vehicle_id1.grid(row = 0, column = 1, padx = 20)
  
  description = Entry(tab1, width = 30)
  description.grid(row = 1, column = 1)
  
  year1= Entry(tab1, width = 30)
  year1.grid(row = 2, column = 1)
  
  type1 = Entry(tab1, width = 30)
  type1.grid(row = 3, column = 1)
  
  category1 = Entry(tab1, width = 30)
  category1.grid(row = 4, column = 1)
  
  #create labels tab1
  vehicle_id_label1 = Label(tab1, text = 'VIN: ')
  vehicle_id_label1.grid(row =0, column = 0)
  
  description_label = Label(tab1, text = 'Description: ')
  description_label.grid(row =1, column = 0)
  
  year_label1 = Label(tab1, text = 'Year: ')
  year_label1.grid(row =2, column = 0)
  
  type_label1 = Label(tab1, text = 'Type: ')
  type_label1.grid(row =3, column = 0)
  
  category_label1 = Label(tab1, text = 'Category: ')
  category_label1.grid(row =4, column = 0)
  
  #add vehicle button 
  submit_btn = Button(tab1, text ='Add Vehicle ', command = submit)
  submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)