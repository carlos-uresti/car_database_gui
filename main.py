
from tkinter import *
from tkinter import ttk

import sqlite3

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


#################################Enter Vehicle############################################

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

##########################################################################################






#################################Enter Customer############################################

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

###############################################################################






####################################Cusomer LookUp##############################

#list query for customers
def input_query2():

	iq_conn = sqlite3.connect('rental.db')

	iq_cur = iq_conn.cursor()

	iq_cur.execute("SELECT Name, Phone FROM CUSTOMER WHERE Name = ? OR Phone = ?",
                (customer_name2.get(), phone_number2.get(),))
  
  #executes search query when list vehicles button is clicked 
	output_records1 = iq_cur.fetchall()

	print_record = ''
  
#print records found
	for output_record1 in output_records1:
		print_record += str(str(output_record1[0])+ " " + output_record1[1]+ " " +"\n")

	iq_label = Label(tab3, text = print_record)

	iq_label.grid(row = 9, column = 0, columnspan = 2)
	
	#commit changes
	iq_conn.commit()
  
	#close the DB connection
	iq_conn.close()

  # input fields 
customer_name2 = Entry(tab3, width = 30)
customer_name2.grid(row = 0, column = 1, padx = 20)

phone_number2 = Entry(tab3, width = 30)
phone_number2.grid(row = 1, column = 1)

#create labels tab1
customer_name_label2 = Label(tab3, text = 'Customer Name: ')
customer_name_label2.grid(row =0, column = 0)

phone_number_label2 = Label(tab3, text = 'Phone Number: ')
phone_number_label2.grid(row =1, column = 0)

#list customer button 
input_qry_btn = Button(tab3, text = 'List Customers', command = input_query2)
input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)
################################################################################





###################################Vehicle Lookup##############################

#list query for vehicles
def input_query():
  
  iq_conn = sqlite3.connect('rental.db')

  iq_cur = iq_conn.cursor()

  iq_cur.execute("SELECT VehicleID, Description, Year, Type, Category FROM VEHICLE WHERE VehicleID = ? OR Description = ? OR Year = ? OR Type = ? OR Category = ?",
                (vehicle_id2.get(), description1.get(), year2.get(), type2.get(), category2.get(),))
  
  #executes search query when list vehicles button is clicked 
  output_records2 = iq_cur.fetchall()
  print_record = ''
  
  
#print records found
  for output_record in output_records2:
	  print_record += str(str(output_record[0])+ " " + output_record[1]+ " " + str(output_record[2])+ " " + str(output_record[3])+ " " + str(output_record[4])+"\n")

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

year2= Entry(tab4, width = 30)
year2.grid(row = 2, column = 1)

type2 = Entry(tab4, width = 30)
type2.grid(row = 3, column = 1)

category2 = Entry(tab4, width = 30)
category2.grid(row = 4, column = 1)

#create labels
vehicle_id_label2 = Label(tab4, text = 'VIN: ')
vehicle_id_label2.grid(row =0, column = 0)

description_label1 = Label(tab4, text = 'Description: ')
description_label1.grid(row =1, column = 0)

year_label2 = Label(tab4, text = 'Year: ')
year_label2.grid(row =2, column = 0)

type_label2 = Label(tab4, text = 'Type: ')
type_label2.grid(row =3, column = 0)

category_label2 = Label(tab4, text = 'Category: ')
category_label2.grid(row =4, column = 0)


input_qry_btn = Button(tab4, text = 'List Vehicles', command = input_query)
input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)
#########################################################################################







###########################################Book Rental##################################
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
  VIN = VIN[1]
  
  
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
  iq_cur.execute("SELECT v.VehicleID, v.Description, v.Year, v.Type, v.Category FROM VEHICLE v, RENTAL r WHERE v.Type = ? AND v.Category = ? AND r.StartDate <= ? AND r.ReturnDate <= ? GROUP BY v.VehicleID",
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

#########################################################################################









###########################################Return Rental####################################



#########################################################################################
#executes tinker components
root.mainloop()
