import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *


def addCustomer():
  #submit new customer info
  def submit2():
  	submit_conn = sqlite3.connect('rental.db')
  
  	submit_cur = submit_conn.cursor()
  
  	submit_cur.execute("INSERT INTO CUSTOMER (Name, Phone) VALUES (:Name, :Phone) ",
  		{
  			'Name': customer_name1.get(),
  			'Phone': phone_number1.get()
  		
  		})
    #commit changes
  	submit_conn.commit()
  	#close the DB connection
  	submit_conn.close()
    
  # input fields 
  customer_name1 = Entry(tab2, width = 30)
  customer_name1.grid(row = 0, column = 1, padx = 20)
  
  phone_number1 = Entry(tab2, width = 30)
  phone_number1.grid(row = 1, column = 1)
  
  #create labels tab1
  customer_name_label1 = Label(tab2, text = 'New Customer Name: ')
  customer_name_label1.grid(row =0, column = 0)
  
  phone_number_label1 = Label(tab2, text = 'Phone Number: ')
  phone_number_label1.grid(row =1, column = 0)
  
  #add customer button 
  submit_btn = Button(tab2, text ='Add Customer ', command = submit2)
  submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

