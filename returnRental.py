import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *

results = StringVar()
customerId = StringVar()
def returnRental():

  def submitReturn():
    global customerId
    Returned = 0
    submit_conn = sqlite3.connect('rental.db')
    submit_cur = submit_conn.cursor()
  
    submit_cur.execute("UPDATE RENTAL SET PaymentDate = 'NULL', Returned = ? WHERE CustID = ? ",(Returned, customerId,))
    #commit changes
    submit_conn.commit()
  	#close the DB connection
    submit_conn.close()

    submitComplete_label = Label(tab6, text = 'Vehicle Return Complete!')
    submitComplete_label.grid(row =13, column = 0, columnspan = 2 )


  
  #list query for vehicles
  def input_query():
    global customerId
    iq_conn = sqlite3.connect('rental.db')
    
    #if Customer Name field is populated, retreive ID for that customer
    if(customer_name.get() != ""):
      iq_cur = iq_conn.cursor()
      iq_cur.execute("SELECT  CustID FROM CUSTOMER WHERE Name = ?", (customer_name.get(),))
      output_records = iq_cur.fetchall()
      customerId = str(output_records[0])
      customerId = customerId.strip("(,)")
    
      #commit changes
      iq_conn.commit()
      
    	#close the DB connection
      iq_conn.close() 
      
    iq_conn = sqlite3.connect('rental.db')
    iq_cur = iq_conn.cursor()
    if(vehicle_id2.get() == "" and description1.get() == "" and year2.get()  == "" and type2.get() == "" and category2.get() == "" and customer_name.get() == ""):
      iq_cur.execute("SELECT * FROM RENTAL")
    else:
      iq_cur.execute("SELECT Name, Year, Description, CASE when PaymentDate='NULL' THEN '($0.00)' ELSE '$'||TotalAmount END FROM VEHICLE V, CUSTOMER C NATURAL JOIN RENTAL R WHERE C.CustID = ? OR V.VehicleID = ? OR V.Description = ? OR V.Year = ? OR V.Type = ? OR V.Category = ? ORDER BY TotalAmount",
                    (customerId, str(vehicle_id2.get()), str(description1.get()), str(year2.get()), str(type2.get()), str(category2.get()),))
    
    #executes search query when list vehicles button is clicked 
    output_records2 = iq_cur.fetchall()
    #print_record = ''
    


    results.set("Select from results")
    drop3 = OptionMenu(tab6, results, *output_records2)
    drop3.grid(row = 9, column =0, columnspan = 2, pady = 5, padx = 10, ipadx = 100)  

    submitRental_qry_btn = Button(tab6, text = 'Submit Return',  command = submitReturn)
    submitRental_qry_btn.grid(row = 11, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)
    
  	#commit changes
    iq_conn.commit()
    
  	#close the DB connection
    iq_conn.close()
  
  # input fields 
  vehicle_id2 = Entry(tab6, width = 30)
  vehicle_id2.grid(row = 0, column = 1, padx = 20)
  
  description1 = Entry(tab6, width = 30)
  description1.grid(row = 1, column = 1)
  
  year2= Entry(tab6, width = 30)
  year2.grid(row = 2, column = 1)
  
  type2 = Entry(tab6, width = 30)
  type2.grid(row = 3, column = 1)
  
  category2 = Entry(tab6, width = 30)
  category2.grid(row = 4, column = 1)
  
  customer_name = Entry(tab6, width = 30)
  customer_name.grid(row = 5, column = 1)

  return_date = Entry(tab6, width = 30)
  return_date.grid(row = 6, column = 1)
  
  #create labels
  vehicle_id_label2 = Label(tab6, text = 'VIN: ')
  vehicle_id_label2.grid(row =0, column = 0)
  
  description_label1 = Label(tab6, text = 'Description: ')
  description_label1.grid(row =1, column = 0)
  
  year_label2 = Label(tab6, text = 'Year: ')
  year_label2.grid(row =2, column = 0)
  
  type_label2 = Label(tab6, text = 'Type: ')
  type_label2.grid(row =3, column = 0)
  
  category_label2 = Label(tab6, text = 'Category: ')
  category_label2.grid(row =4, column = 0)

  customer_name_label = Label(tab6, text = 'Customer Name: ')
  customer_name_label.grid(row =5, column = 0)

  return_date_label = Label(tab6, text = 'Return Date: ')
  return_date_label.grid(row =6, column = 0)
  
  
  input_qry_btn = Button(tab6, text = 'List Vehicle', command = input_query)
  input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)