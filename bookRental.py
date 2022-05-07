import os
import sys
import sqlite3
from tkinter import *
from tkinter import ttk
from tabs import *



def bookRental():
  payDate = StringVar()

  vehicle3 =StringVar()
  
  total = IntVar()
  
  def calcTotal(event):
    global total
    carType = type3.get()
    category = category3.get()
    rentalType = rentalType4.get()
    if carType == 'Compact': 
      carType = "1" 
  
    elif carType == "Medium": 
      carType = "2"
  
    elif carType == "Large": 
      carType = "3" 
      
    elif carType == "SUV": 
      carType = "4"
       
    elif carType == "Truck": 
      carType = "5"
  
    elif carType == "VAN": 
      carType = "6"  
  
    if category == 'Basic': 
      category = "0" 
  
    elif category == "Luxury": 
      category = "1"
  
    iq_conn = sqlite3.connect('rental.db')
    iq_cur = iq_conn.cursor()
    if rentalType == "Weekly":
      iq_cur.execute("SELECT Weekly FROM RATE WHERE Type = ? AND Category = ?",
                    (carType, category,))
    elif rentalType == "Daily":
      iq_cur.execute("SELECT Daily FROM RATE WHERE Type = ? AND Category = ?",
                    (carType, category,))  
    #executes search query when list vehicles button is clicked 
    rates = iq_cur.fetchall()
    arr = rates[0]
    #commit changes
    iq_conn.commit()
  	#close the DB connection
    iq_conn.close()
    
    #calculate total amount for rental and place it in label
    total = int(arr[0]) * int(quantity.get())
    
    payDate.set("Total = " + str(total))
  
  def reserve_query():
  
    global vehicle3
    arr = vehicle3.get().split(',')
    VIN = arr[0].split('(')
    VIN = VIN[1].replace("'", "")
    print(VIN)
      
    print("Total", total)
    #weekly or daily rental, convert to numeric representation
    rentalType = rentalType4.get()
    
    if rentalType == "Daily":
      rentalType = "1"
    elif rentalType == "Weekly": 
      rentalType = "7"
  
    #answer to whether cusomter wants to pay today or on return of vehicle
    
    
      
    submit_conn = sqlite3.connect('rental.db')
    submit_cur = submit_conn.cursor()
    submit_cur.execute("INSERT INTO RENTAL VALUES (:CustID, :VehicleID, :StartDate, :OrderDate, :RentalType, :Qty, :ReturnDate, :TotalAmount, :PaymentDate) ",
  		{
  			'CustID': customerId.get(),
  			'VehicleID': VIN,
  			'StartDate': startDate.get(),
  			'OrderDate': orderDate.get(),
  			'RentalType': rentalType,
        'Qty': quantity.get(),
        'ReturnDate': endDate.get(),
        'TotalAmount': total,
        'PaymentDate': orderDate.get(),
  		})
    #commit changes
    submit_conn.commit()
  	#close the DB connection
    submit_conn.close()
    
  
  
  
  #list query for vehicles
  carType = StringVar()
  category = StringVar()
  
  def input_query():
    
    carType = type3.get()
    category = category3.get()
    
    if carType == 'Compact': 
      carType = "1" 
  
    elif carType == "Medium": 
      carType = "2"
  
    elif carType == "Large": 
      carType = "3" 
      
    elif carType == "SUV": 
      carType = "4"
       
    elif carType == "Truck": 
      carType = "5"
  
    elif carType == "VAN": 
      carType = "6"  
  
    if category == 'Basic': 
      category = "0" 
  
    elif category == "Luxury": 
      category = "1"  
  
    iq_conn = sqlite3.connect('rental.db')
    iq_cur = iq_conn.cursor()
    iq_cur.execute("SELECT v.VehicleID, v.Description, v.Year, v.Type, v.Category FROM VEHICLE v, RENTAL r WHERE v.Type = ? AND v.Category = ? AND r.StartDate < ? AND r.ReturnDate > ? GROUP BY v.VehicleID",
                  (carType, category, startDate.get(), endDate.get(),))
    
    #executes search query when list vehicles button is clicked 
    output_records3 = iq_cur.fetchall()
    
    #commit changes
    iq_conn.commit()
  	#close the DB connection
    iq_conn.close()
    
    vehicle3.set("Select from results")
    drop3 = OptionMenu(tab5, vehicle3, *output_records3)
    drop3.grid(row = 9, column =1, columnspan = 2, pady = 5, padx = 10, ipadx = 100)
  
    payOptions = ["Pay Today", "Pay On Return"]
    
    payDate.set("Pay Now or Later")
    payDrop = OptionMenu(tab5, payDate, *payOptions, command = calcTotal)
    payDrop.grid(row = 11, column =1, columnspan = 2, pady = 5, padx = 10, ipadx = 100)
    
    reserve_qry_btn = Button(tab5, text = 'Reserve Vehicle', command = reserve_query)
    reserve_qry_btn.grid(row = 13, column =1, columnspan = 1, pady = 10, padx = 5, ipadx = 100)
  
  
  # input fields
  customerId = Entry(tab5, width = 30)
  customerId.grid(row = 0, column = 1)
  
  startDate = Entry(tab5, width = 30)
  startDate.grid(row = 1, column = 1)
  
  endDate = Entry(tab5, width = 30)
  endDate.grid(row = 2, column = 1)
  
  orderDate = Entry(tab5, width = 30)
  orderDate.grid(row = 3, column = 1)
  
  #vehicle type drop down menu	
  vehicleTypes = ["Compact", "Medium", "Large", "SUV", "Truck", "VAN"]
  type3 = StringVar()
  type3.set("Vehicle Type")
  drop = OptionMenu(tab5, type3, *vehicleTypes)
  drop.grid(column = 1, row=4 )
  
  #vehicle category dropdown menu
  vehicleCategories = ['Basic', 'Luxury']
  category3 = StringVar()
  category3.set("Vehicle Category")
  drop2 = OptionMenu(tab5, category3, *vehicleCategories)
  drop2.grid(column = 1, row= 5)
  
  #vehicle category dropdown menu
  vehicleRentalType = ["Daily", "Weekly"]
  rentalType4 = StringVar()
  rentalType4.set("Rental Type")
  drop2 = OptionMenu(tab5, rentalType4, *vehicleRentalType)
  drop2.grid(column = 1, row= 6)
  
  quantity = Entry(tab5, width = 30)
  quantity.grid(row = 7, column = 1)
  
  #create labels
  customerId_label = Label(tab5, text = 'Customer ID: ')
  customerId_label.grid(row =0, column = 0)
  
  startDate_label = Label(tab5, text = 'Start Date**: ')
  startDate_label.grid(row =1, column = 0)
  
  endDate_label = Label(tab5, text = 'End Date**: ')
  endDate_label.grid(row =2, column = 0)
  
  orderDate_label = Label(tab5, text = 'Order Date: ')
  orderDate_label.grid(row = 3, column = 0)
  
  type_label3 = Label(tab5, text = 'Type**: ')
  type_label3.grid(row =4, column = 0)
  
  category_label3 = Label(tab5, text = 'Category**: ')
  category_label3.grid(row =5, column = 0)
  
  vehicle_rental_label = Label(tab5, text = 'Rental Type: ')
  vehicle_rental_label.grid(row =6, column = 0)
  
  quantity_label = Label(tab5, text = 'Quantity')
  quantity_label.grid(row = 7,  column =  0)
  
  #create another dropdown that displays results in a select menu rather than print them
  input_qry_btn = Button(tab5, text = 'Search available vehicles', command = input_query)
  input_qry_btn.grid(row = 8, column =1, columnspan = 1, pady = 10, padx = 10, ipadx = 100)
  #results dropdown menu
