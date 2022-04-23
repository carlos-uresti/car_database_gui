
# -- PyQt5 pip install PyQt5

# -- Tkinter pip install tkinter 

# -- Kivy   pip install kivy


from tkinter import *

import sqlite3


# create tkinter window 

root = Tk()

root.title('Address Book')

root.geometry("400x400")



address_book_connect = sqlite3.connect('address_book.db')

address_book_cur = address_book_connect.cursor()


# address_book_cur.execute('''CREATE TABLE addresses(
# 							first_name text,
# 							last_name text,
# 							street text,
# 							city text,
# 							state text,
# 							zipcode integer)''')


def submit():
	submit_conn = sqlite3.connect('address_book.db')

	submit_cur = submit_conn.cursor()

	submit_cur.execute("INSERT INTO ADDRESSES VALUES (:fname, :lname, :street, :city, :state, :zcode) ",
		{
			'fname': f_name.get(),
			'lname': l_name.get(),
			'street': street.get(),
			'city': city.get(),
			'state': state.get(),
			'zcode': zipcode.get()
		})

	#commit changes

	submit_conn.commit()
	#close the DB connection
	submit_conn.close()



def input_query():

	iq_conn = sqlite3.connect('address_book.db')

	iq_cur = iq_conn.cursor()

	iq_cur.execute("SELECT first_name, last_name FROM ADDRESSES WHERE state = ? AND city = ?", 
						(state.get(), city.get(),))

	output_records = iq_cur.fetchall()

	print_record = ''

	for output_record in output_records:
		print_record += str(output_record[0]+ " " + output_record[1]+"\n")

	iq_label = Label(root, text = print_record)

	iq_label.grid(row = 9, column = 0, columnspan = 2)
	
	#commit changes

	iq_conn.commit()
	#close the DB connection
	iq_conn.close()


#building the gui components
	# pack place grid

	# create text boxes

f_name = Entry(root, width = 30)
f_name.grid(row = 0, column = 1, padx = 20)


l_name = Entry(root, width = 30)
l_name.grid(row = 1, column = 1)

street= Entry(root, width = 30)
street.grid(row = 2, column = 1)

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

state = Entry(root, width = 30)
state.grid(row = 4, column = 1)

zipcode= Entry(root, width = 30)
zipcode.grid(row = 5, column = 1)

	#create label

f_name_label = Label(root, text = 'First Name: ')
f_name_label.grid(row =0, column = 0)

l_name_label = Label(root, text = 'Last Name: ')
l_name_label.grid(row =1, column = 0)

street_label = Label(root, text = 'Street: ')
street_label.grid(row =2, column = 0)

city_label = Label(root, text = 'City: ')
city_label.grid(row =3, column = 0)

state_label = Label(root, text = 'State: ')
state_label.grid(row =4, column = 0)

zcode_label = Label(root, text = 'Zipcode: ')
zcode_label.grid(row =5, column = 0)


submit_btn = Button(root, text ='Add Contact ', command = submit)
submit_btn.grid(row = 7, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)

input_qry_btn = Button(root, text = 'Output Names', command = input_query)
input_qry_btn.grid(row = 8, column =0, columnspan = 2, pady = 10, padx = 10, ipadx = 140)



#executes tinker components
root.mainloop()
