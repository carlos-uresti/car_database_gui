import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *



def listVehicles():
  #list query for vehicles
  Empty = False;
  def input_query():
    
    iq_conn = sqlite3.connect('rental.db')
  
    iq_cur = iq_conn.cursor()
    if(vehicle_id2.get() == "" and description1.get() == "" ):
      Empty = True;
      iq_cur.execute("select VIN, Vehicle, printf('$%0.2f', OrderAmount / TotalDays) as [DAILY] from vRentalInfo")
    else:
      Empty = False;
      iq_cur.execute("select VIN, Vehicle, printf('$%0.2f', OrderAmount / TotalDays) as [DAILY] from vRentalInfo WHERE VIN = ? OR VEHICLE = ?",
                    (vehicle_id2.get(), description1.get(),))
    
    #executes search query when list vehicles button is clicked 
    output_records2 = iq_cur.fetchall()
    print_record = ''
    
    
  #print records found
    for output_record in output_records2:
      if Empty:
  	    print_record += str(str(output_record[0])+ " " + output_record[1]+ " " + str(output_record[2])+ " " + "\n")
      else:
        print_record += str(str(output_record[0])+ " " + output_record[1]+ str(output_record[2])+ " " + "\n")
  
    iq_label = Label(tab4, text = print_record)
  
    iq_label.grid(row = 9, column = 0, columnspan = 2)
  	
  	#commit changes
    iq_conn.commit()
    
  	#close the DB connection
    iq_conn.close()
  
  
  records = [""]
  
  # input fields 
  vehicle_id2 = Entry(tab4, width = 30)
  vehicle_id2.grid(row = 0, column = 1, padx = 20)
  
  description1 = Entry(tab4, width = 30)
  description1.grid(row = 1, column = 1)
  
  
  #create labels
  vehicle_id_label2 = Label(tab4, text = 'VIN: ')
  vehicle_id_label2.grid(row =0, column = 0)
  
  description_label1 = Label(tab4, text = 'Description: ')
  description_label1.grid(row =1, column = 0)
  
  
  
  
  input_qry_btn = Button(tab4, text = 'List Vehicles', command = input_query)
  input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)