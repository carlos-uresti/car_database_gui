
from tkinter import *
from tkinter import ttk

import sqlite3

# create tkinter window 
root = Tk()

root.title('Car Rental Database 2019')

root.geometry("600x1200")

#note book with tabs for each function of database
car_database = ttk.Notebook(root)
car_database.pack()#inflates database notebook

#add vehicle tab
tab1 = Frame(car_database, width=600, height = 600)
#add customer tab
tab2 = Frame(car_database, width=600, height = 600)
#customer lookup tab
tab3 = Frame(car_database, width=600, height = 600)
#vehicle lookup tab
tab4 = Frame(car_database, width=600, height = 600)
#book rental tab
tab5 = Frame(car_database, width=600, height = 600)
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
			'VehicleID': vehicle_id.get(),
			'Description': description.get(),
			'Year': year.get(),
			'Type': type.get(),
			'Category': category.get()
		
		})
  #commit changes
	submit_conn.commit()
	#close the DB connection
	submit_conn.close() 
# input fields 
vehicle_id = Entry(tab1, width = 30)
vehicle_id.grid(row = 0, column = 1, padx = 20)


description = Entry(tab1, width = 30)
description.grid(row = 1, column = 1)

year= Entry(tab1, width = 30)
year.grid(row = 2, column = 1)

type = Entry(tab1, width = 30)
type.grid(row = 3, column = 1)

category = Entry(tab1, width = 30)
category.grid(row = 4, column = 1)

#create labels tab1
vehicle_id_label = Label(tab1, text = 'VIN: ')
vehicle_id_label.grid(row =0, column = 0)

description_label = Label(tab1, text = 'Description: ')
description_label.grid(row =1, column = 0)

year_label = Label(tab1, text = 'Year: ')
year_label.grid(row =2, column = 0)

type_label = Label(tab1, text = 'Type: ')
type_label.grid(row =3, column = 0)

category_label = Label(tab1, text = 'Category: ')
category_label.grid(row =4, column = 0)

#add vehicle button 
submit_btn = Button(tab1, text ='Add Vehicle ', command = submit)
submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

##########################################################################################




#################################Enter Customer############################################

#submit new customer info
def submit2():
	submit_conn = sqlite3.connect('rental.db')

	submit_cur = submit_conn.cursor()

	submit_cur.execute("INSERT INTO CUSTOMER VALUES (:Name, :Phone) ",
		{
			'Name': customer_name.get(),
			'Phone': phone_number.get()
		
		})
  #commit changes
	submit_conn.commit()
	#close the DB connection
	submit_conn.close()
  
# input fields 
customer_name = Entry(tab2, width = 30)
customer_name.grid(row = 0, column = 1, padx = 20)

phone_number = Entry(tab2, width = 30)
phone_number.grid(row = 1, column = 1)

#create labels tab1
customer_name_label = Label(tab2, text = 'New Customer Name: ')
customer_name_label.grid(row =0, column = 0)

phone_number_label = Label(tab2, text = 'Phone Number: ')
phone_number_label.grid(row =1, column = 0)

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
                (customer_name.get(), phone_number.get(),))
  
  #executes search query when list vehicles button is clicked 
	output_records = iq_cur.fetchall()

	print_record = ''
  
#print records found
	for output_record in output_records:
		print_record += str(str(output_record[0])+ " " + output_record[1]+ " " +"\n")

	iq_label = Label(tab3, text = print_record)

	iq_label.grid(row = 9, column = 0, columnspan = 2)
	
	#commit changes
	iq_conn.commit()
  
	#close the DB connection
	iq_conn.close()

  # input fields 
customer_name = Entry(tab3, width = 30)
customer_name.grid(row = 0, column = 1, padx = 20)

phone_number = Entry(tab3, width = 30)
phone_number.grid(row = 1, column = 1)

#create labels tab1
customer_name_label = Label(tab3, text = 'Customer Name: ')
customer_name_label.grid(row =0, column = 0)

phone_number_label = Label(tab3, text = 'Phone Number: ')
phone_number_label.grid(row =1, column = 0)

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
                (vehicle_id.get(), description.get(), year.get(), type.get(), category.get(),))
  
  #executes search query when list vehicles button is clicked 
  output_records = iq_cur.fetchall()
  print_record = ''
  
  
#print records found
  for output_record in output_records:
	  print_record += str(str(output_record[0])+ " " + output_record[1]+ " " + str(output_record[2])+ " " + str(output_record[3])+ " " + str(output_record[4])+"\n")

  iq_label = Label(tab4, text = print_record)

  iq_label.grid(row = 9, column = 0, columnspan = 2)
	
	#commit changes
  iq_conn.commit()
  
	#close the DB connection
  iq_conn.close()


records = [""]

# input fields 
vehicle_id = Entry(tab4, width = 30)
vehicle_id.grid(row = 0, column = 1, padx = 20)

description = Entry(tab4, width = 30)
description.grid(row = 1, column = 1)

year= Entry(tab4, width = 30)
year.grid(row = 2, column = 1)

type = Entry(tab4, width = 30)
type.grid(row = 3, column = 1)

category = Entry(tab4, width = 30)
category.grid(row = 4, column = 1)

#create labels
vehicle_id_label = Label(tab4, text = 'VIN: ')
vehicle_id_label.grid(row =0, column = 0)

description_label = Label(tab4, text = 'Description: ')
description_label.grid(row =1, column = 0)

year_label = Label(tab4, text = 'Year: ')
year_label.grid(row =2, column = 0)

type_label = Label(tab4, text = 'Type: ')
type_label.grid(row =3, column = 0)

category_label = Label(tab4, text = 'Category: ')
category_label.grid(row =4, column = 0)


input_qry_btn = Button(tab4, text = 'List Vehicles', command = input_query)
input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)
#########################################################################################




###########################################Book Rental###################################


#list query for vehicles
def input_query():
  iq_conn = sqlite3.connect('rental.db')
  iq_cur = iq_conn.cursor()
  iq_cur.execute("SELECT v.VehicleID, v.Description, v.Year, v.Type, v.Category FROM VEHICLE v, RENTAL r WHERE v.Type = ? AND v.Category = ? AND r.StartDate <= ? AND r.ReturnDate <= ? GROUP BY v.VehicleID",
                (type.get(), category.get(), startDate.get(), endDate.get(),))
  
  #executes search query when list vehicles button is clicked 
  output_records = iq_cur.fetchall()
  #commit changes
  iq_conn.commit()
	#close the DB connection
  iq_conn.close()
  
  vehicle = StringVar()
  vehicle.set("Select from results")
  drop3 = OptionMenu(tab5, vehicle, *output_records)
  drop3.grid(row = 10, column =1, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



# input fields
customerId = Entry(tab5, width = 30)
customerId.grid(row = 0, column = 1)

customerName = Entry(tab5, width = 30)
customerName.grid(row = 1, column = 1)

startDate = Entry(tab5, width = 30)
startDate.grid(row = 2, column = 1, padx = 20)

endDate = Entry(tab5, width = 30)
endDate.grid(row = 3, column = 1)

#create labels
customerId_label = Label(tab5, text = 'Customer ID: ')
customerId_label.grid(row =0, column = 0)

customer_name_label = Label(tab5, text = 'Customer Name: ')
customer_name_label.grid(row =1, column = 0)

startDate_label = Label(tab5, text = 'Start Date: ')
startDate_label.grid(row =2, column = 0)

endDate_label = Label(tab5, text = 'End Date: ')
endDate_label.grid(row =3, column = 0)

type_label = Label(tab5, text = 'Type: ')
type_label.grid(row =4, column = 0)

category_label = Label(tab5, text = 'Category: ')
category_label.grid(row =5, column = 0)

#vehicle type drop down menu	
vehicleTypes = ["1", "2", "3", "4", "5", "6"]
type = StringVar()
type.set("Vehicle Type")
drop = OptionMenu(tab5, type, *vehicleTypes)
drop.grid(column = 1, row=4 )

#vehicle category dropdown menu
vehicleCategories = ["0", "1"]
category = StringVar()
category.set("Vehicle Category")
drop2 = OptionMenu(tab5, category, *vehicleCategories)
drop2.grid(column = 1, row= 5)


#create another dropdown that displays results in a select menu rather than print them
input_qry_btn = Button(tab5, text = 'Search available vehicles', command = input_query)
input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

#results dropdown menu


#########################################################################################


###########################################Return Rental####################################



#########################################################################################
#executes tinker components
root.mainloop()
