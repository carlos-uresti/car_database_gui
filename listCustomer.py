import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *

iq_label = Label(root)  # needed to clear
Empty = False
names = []
def listCustomer():
  iq_conn = sqlite3.connect('rental.db')
  iq_cur = iq_conn.cursor()
  # global iq_label

  def all_cust():
    
    global iq_label
    iq_label.destroy() # needed to clear
    print_record = '' 
    iq_cur.execute("SELECT * FROM Customer")
    output_records1 = iq_cur.fetchall()
    count = 0
    for output_record1 in output_records1:
        print_record += '| {:^10s} | {:^15s} | {:^8s} |'.format(str(output_record1[0]), str(output_record1[1]),  str(
            output_record1[2])) + '\n'
        count += 1
    print_record += f"Records returned: {count}"

    iq_label = Label(tab3, text=print_record)

    iq_label.grid(row=10, column=0, columnspan=2)
    #commit changes
    iq_conn.commit()

    #close the DB connection
    

  def input_query2():
    
    global iq_label  # needed to clear
    iq_label.destroy() # needed to clear
    print_record = ''  # needed to clear

    #set condition to account for empty fields
    if(customer_name2.get() == "" and customer_id.get()== ""):
      Empty = True
      iq_cur.execute(
          "SELECT CustomerID, CustomerName, CASE when RentalBalance = 0 THEN '$0.00' ELSE '$'||RentalBalance END FROM vRentalInfo ORDER BY RentalBalance")
      
    else:
      Empty = False
      cust_name_text = customer_name2.get()
      cust_id_text = customer_id.get()
      if cust_name_text and not cust_id_text:
        iq_cur.execute("SELECT CustomerID, CustomerName, CASE when RentalBalance = 0 THEN '$0.00' ELSE '$'||RentalBalance END FROM vRentalInfo WHERE CustomerName LIKE ?",
                       ('%'+cust_name_text+'%',))
      elif cust_id_text and not cust_name_text:
        iq_cur.execute("SELECT CustomerID, CustomerName, CASE when RentalBalance = 0 THEN '$0.00' ELSE '$'||RentalBalance END FROM vRentalInfo WHERE CustomerID = ?",
                       (cust_id_text,))
      else:
        print_record += "CAN ONLY SEARCH ONE FILTER\n"
    
    #executes search query when list vehicles button is clicked 
    output_records1 = iq_cur.fetchall()
    
    count = 0  
  #print records found
    for output_record1 in output_records1:
      if Empty:
        print_record += '| {:^10s} | {:^15s} | {:^8s} |'.format(str(output_record1[0]), str(output_record1[1]),  str(
            output_record1[2])) + '\n'
        count += 1
      else:
        print_record += '| {:^10s} | {:^15s} | {:^8s} |'.format(str(output_record1[0]), str(output_record1[1]),  str(
            output_record1[2])) + '\n'
        count += 1
    print_record += f"Records returned: {count}"
  
    iq_label = Label(tab3, text = print_record)
    
    iq_label.grid(row = 10, column = 0, columnspan = 2)
  	
  	#commit changes
    iq_conn.commit()
    
  	#close the DB connection
    
  
    # input fields 
  customer_name2 = Entry(tab3, width = 30)
  customer_name2.grid(row = 0, column = 1, padx = 20)
  
  customer_id = Entry(tab3, width=30)
  customer_id.grid(row=1, column=1)
  
  #create labels tab1
  customer_name_label2 = Label(tab3, text = 'Customer Name: ')
  customer_name_label2.grid(row =0, column = 0)
  
  customer_id_label2 = Label(tab3, text = 'Customer ID: ')
  customer_id_label2.grid(row=1, column=0)
  
  #list customer button 
  input_qry_btn = Button(tab3, text='List Customers', command=input_query2)
  input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

  #list ALL customer button
  all_cust_btn = Button(tab3, text='List ALL Customers', command=all_cust)
  all_cust_btn.grid(row=9, column=0, columnspan=2,
                     pady=10, padx=10, ipadx=140)
