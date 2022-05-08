import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *


def listCustomer():
  #list query for customers
  Empty = False
  def input_query2():

    iq_conn = sqlite3.connect('rental.db')
    iq_cur = iq_conn.cursor()

    #set condition to account for empty fields
    if(customer_name2.get() == "" and customer_id.get()== ""):
      Empty = True
      iq_cur.execute("SELECT CustID, Name, CASE when PaymentDate='NULL' THEN '$0.00' ELSE '$'||TotalAmount END FROM CUSTOMER NATURAL JOIN RENTAL ORDER BY TotalAmount")
    else:
      Empty = False
      iq_cur.execute("SELECT CustID, Name FROM CUSTOMER WHERE Name = ? OR CustID = ?",
                  (customer_name2.get(), customer_id.get(),))    
    
    #executes search query when list vehicles button is clicked 
    output_records1 = iq_cur.fetchall()
  
    print_record = ''
    
  #print records found
    for output_record1 in output_records1:
      if Empty:
        print_record += str(str(output_record1[0])+ " " + str(output_record1[1])+ " " + str(output_record1[2]) +"\n")
      else:
        print_record += str(str(output_record1[0])+ " " + str(output_record1[1])+ "" +"\n")
  
    iq_label = Label(tab3, text = print_record)
  
    iq_label.grid(row = 9, column = 0, columnspan = 2)
  	
  	#commit changes
    iq_conn.commit()
    
  	#close the DB connection
    iq_conn.close()
  
    # input fields 
  customer_name2 = Entry(tab3, width = 30)
  customer_name2.grid(row = 0, column = 1, padx = 20)
  
  customer_id = Entry(tab3, width = 30)
  customer_id.grid(row = 1, column = 1)
  
  #create labels tab1
  customer_name_label2 = Label(tab3, text = 'Customer Name: ')
  customer_name_label2.grid(row =0, column = 0)
  
  customer_id_label2 = Label(tab3, text = 'Customer ID: ')
  customer_id_label2.grid(row =1, column = 0)
  
  #list customer button 
  input_qry_btn = Button(tab3, text = 'List Customers', command = input_query2)
  input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)