from Ui import *
from PyQt5.QtWidgets import *
import mysql.connector
import sys
import datetime
import time

listahan = []
quants = []
outofstock = []
totalsss = []

class BS(Ui_MainWindow, QMainWindow):
	def __init__(self):
		super(Ui_MainWindow, self).__init__()
		self.setupUi(self)

		#DBCONNECTION
		self.conn = mysql.connector.connect(host="localhost", user="root", passwd="narag", database="bsinventory")

		#MainPageButtons
		self.adminBtn.clicked.connect(self.adminshow)
		self.staffBtn.clicked.connect(self.staffshow)
		self.cashierBtn.clicked.connect(self.cashiershow)
		self.exit.clicked.connect(self.exitnow)

		#BackButtons
		self.backBtn.clicked.connect(self.back1)
		self.backBtn_2.clicked.connect(self.back2)
		self.backBtn_3.clicked.connect(self.back3)

		#Admin
		self.loginBtn.clicked.connect(self.showadmin)
		self.back.clicked.connect(self.adminback)
		self.userName.textChanged.connect(self.errorBlank)
		self.passWord.textChanged.connect(self.errorBlank)
		self.pushButton.clicked.connect(self.adminadd)
		self.pushButton_2.clicked.connect(self.admindel)
		self.loginBtn.setEnabled(False)

		# Staff
		self.loginBtn_2.clicked.connect(self.showstaff)
		self.backBtn_staff.clicked.connect(self.backstaff)
		self.addItembtn.clicked.connect(self.staffadd)
		self.userName_2.textChanged.connect(self.errorBlank)
		self.passWord_2.textChanged.connect(self.errorBlank)
		self.lineEdit.textChanged.connect(self.errorBlank)
		self.loginBtn_2.setEnabled(False)
		self.addItembtn.setEnabled(False)
		self.addItembtn.setEnabled(False)

		# Cashier
		self.loginBtn_3.clicked.connect(self.showcashier)
		self.backtomain_2.clicked.connect(self.backcashier)
		self.userName_3.textChanged.connect(self.errorBlank)
		self.passWord_3.textChanged.connect(self.errorBlank)
		self.customername.textChanged.connect(self.errorBlank)
		self.addorder.clicked.connect(self.cashieradd)
		self.paymentpaid.clicked.connect(self.payment)
		self.paymentpaid_3.clicked.connect(self.clear)
		self.loginBtn_3.setEnabled(False)
		self.addorder.setEnabled(False)
		self.paymentpaid.setEnabled(False)

		self.totals = 0
		self.toalsales = 0
		self.orders = []
	# --------------------------------------------------------------------------------------------------------------#
		connection1 = self.conn.cursor()
		connection1.execute("select itemname,quantity,price from products;")
		self.items.setRowCount(0)
		for row_number, row_data in enumerate(connection1):
			self.items.insertRow(row_number)
			for colum_number, data in enumerate(row_data):
				self.items.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

		connection2 = self.conn.cursor()
		connection2.execute("select itemname,quantity,price from products;")
		self.items_2.setRowCount(0)
		for row_number, row_data in enumerate(connection2):
			self.items_2.insertRow(row_number)
			for colum_number, data in enumerate(row_data):
				self.items_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

		connection3 = self.conn.cursor()
		connection3.execute("select name,datetime,amount from orders;")
		self.items_3.setRowCount(0)
		for row_number, row_data in enumerate(connection3):
			self.items_3.insertRow(row_number)
			for colum_number, data in enumerate(row_data):
				self.items_3.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

		connection4 = self.conn.cursor()
		connection4.execute("select itemname from outofstocks;")
		self.items_5.setRowCount(0)
		for row_number, row_data in enumerate(connection4):
			self.items_5.insertRow(row_number)
			for colum_number, data in enumerate(row_data):
				self.items_5.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

		connection5 = self.conn.cursor()
		connection5.execute("select datetime,totalsales from totalsales;")
		self.items_4.setRowCount(0)
		for row_number, row_data in enumerate(connection5):
			self.items_4.insertRow(row_number)
			for colum_number, data in enumerate(row_data):
				self.items_4.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

	# --------------------------------------------------------------------------------------------------------------#
	def errorBlank(self):
		if self.userName.text() and self.userName.text().strip() and self.passWord.text() and self.passWord.text().strip():
			self.loginBtn.setEnabled(True)
		else:
			self.loginBtn.setEnabled(False)
		if self.userName_2.text() and self.userName_2.text().strip() and self.passWord_2.text() and \
				self.passWord_2.text().strip():

			self.loginBtn_2.setEnabled(True)
		else:
			self.loginBtn_2.setEnabled(False)
		if self.userName_3.text() and self.userName_3.text().strip() and self.passWord_3.text() and \
				self.passWord_3.text().strip():

			self.loginBtn_3.setEnabled(True)
		else:
			self.loginBtn_3.setEnabled(False)
		if self.lineEdit.text() and self.lineEdit.text().strip():
			self.addItembtn.setEnabled(True)
		else:
			self.addItembtn.setEnabled(False)
		if self.customername.text() and self.customername.text().strip():
			self.addorder.setEnabled(True)
		else:
			self.addorder.setEnabled(False)
	# --------------------------------------------------------------------------------------------------------------#

	def adminshow(self):
		self.stackedWidget.setCurrentIndex(3)
	def staffshow(self):
		self.stackedWidget.setCurrentIndex(4)
	def cashiershow(self):
		self.stackedWidget.setCurrentIndex(5)
	def exitnow(self):
		exit1 = QMessageBox.question(self, "Closed Apps", "Are you sure you want to exit the program?",
									 QMessageBox.Yes | QMessageBox.No)
		if exit1 == QMessageBox.Yes:
			qApp.quit()

	def back1(self):
		self.stackedWidget.setCurrentIndex(0)
	def back2(self):
		self.stackedWidget.setCurrentIndex(0)
	def back3(self):
		self.stackedWidget.setCurrentIndex(0)

	# --------------------------------------------------------------------------------------------------------------#

	def showadmin(self):
		txt1 = self.userName.text()
		txt2 = self.passWord.text()
		if txt1 and txt2 != 'admin':
			QMessageBox.warning(self, "Invalid Credentials", "Please Input All the Necessary Information Needed!")
			self.userName.clear()
			self.passWord.clear()
		else:
			self.stackedWidget.setCurrentIndex(6)
			self.userName.clear()
			self.passWord.clear()

	def adminback(self):
		self.stackedWidget.setCurrentIndex(3)

	def showstaff(self):
		txt1 = self.userName_2.text()
		txt2 = self.passWord_2.text()
		if txt1 and txt2 != 'staff':
			QMessageBox.warning(self,"Invalid Credentials","Please Input All the Necessary Information Needed!")
			self.userName_2.clear()
			self.passWord_2.clear()
		else:
			self.stackedWidget.setCurrentIndex(1)
			self.userName_2.clear()
			self.passWord_2.clear()

	def backstaff(self):
		self.stackedWidget.setCurrentIndex(4)

	def showcashier(self):
		txt1 = self.userName_3.text()
		txt2 = self.passWord_3.text()
		if txt1 and txt2 != 'cashier':
			QMessageBox.warning(self, "Invalid Credentials", "Please Input All the Necessary Information Needed!")
			self.userName_3.clear()
			self.passWord_3.clear()
		else:
			self.stackedWidget.setCurrentIndex(2)
			self.userName_3.clear()
			self.passWord_3.clear()

	def backcashier(self):
		self.stackedWidget.setCurrentIndex(5)

	# --------------------------------------------------------------------------------------------------------------#

	def staffadd(self):
		item1 = self.lineEdit.text()
		item2 = self.spinBox.value()
		item3 = self.price.value()

		connection = self.conn.cursor()
		connections = self.conn.cursor()

		check = "SELECT * FROM products where itemname=%s;"
		data = (item1,)
		connection.execute(check,data)
		go = connection.fetchall()
		c = len(go)
		if c > 0:
			QMessageBox.warning(self, "Invalid Credentials", "It is already in the database!")
			self.lineEdit.clear()
		elif item1.isnumeric() == True:
			QMessageBox.warning(self, "Invalid Credentials", "Numeric are not alowed!")
			self.lineEdit.clear()
		else:
			add = "insert into products(itemname, quantity, price) values(%s, %s, %s);"
			data = (item1, item2, item3)
			connection.execute(add, data)
			self.conn.commit()
			QMessageBox.about(self, "Added Successfully", "The Product was added Successfully")

			listahan.append([item1,item3])
			quants.append(item2)
			self.comboBox.addItem(item1)

			self.spinBox.setValue(1)
			self.price.setValue(1)

			self.lineEdit.clear()

			connection.execute("select itemname,quantity,price from products;")
			self.items.setRowCount(0)
			for row_number, row_data in enumerate(connection):
				self.items.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

			connections.execute("select itemname,quantity,price from products;")
			self.items_2.setRowCount(0)
			for row_number, row_data in enumerate(connections):
				self.items_2.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

			check = "SELECT * FROM outofstocks where itemname=%s;"
			data = (item1,)
			connection.execute(check, data)
			go = connection.fetchall()
			c = len(go)
			if c > 0:
				chk = "delete from outofstocks where itemname=%s"
				data = (item1,)
				connection.execute(chk, data)
				self.conn.commit()

				connection.execute("select itemname from outofstocks;")
				self.items_5.setRowCount(0)
				for row_number, row_data in enumerate(connection):
					self.items_5.insertRow(row_number)
					for colum_number, data in enumerate(row_data):
						self.items_5.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
			else:
				pass

	# --------------------------------------------------------------------------------------------------------------#

	def cashieradd(self):
		item1 = self.customername.text()
		item2 = self.comboBox.currentText()
		item3 = self.quantity_2.value()
		date = datetime.datetime.now()

		if item1.isnumeric() == True:
			QMessageBox.warning(self, "Invalid Credentials", "Don't input numeric in names")
		elif item2 == "":
			QMessageBox.warning(self, "Invalid Credentials", "There's no available items for now")
		else:
			x = 0
			go = 0
			for i in range(len(listahan)):
				if item2 == listahan[i][0]:
					go = i
					x = listahan[i][1]
			chk1 = quants[go]
			chk2 = x

			if item3 > chk1:
				QMessageBox.warning(self,"Not Enough Stocks Available!",str(item2) + "------" + str(chk1) +"-"+ "stock/s are available.")
				self.quantity_2.setValue(chk1)

			else:
				total = chk2 * item3
				orders = chk1 - item3
				quants[go] = orders
				self.orders.append(str(item2) + "-----" + str(orders) + "....." + "P " + str(total) + "0")
				self.listoforder.addItem(str(item2) + "-----" + str(orders) + "....." + "P " + str(total) + "0")
				self.totals += total
				totalsss.append(total)
				self.amount.setText(str(self.totals)+"0")
				self.paymentpaid.setEnabled(True)

				connection = self.conn.cursor()

				add1 = "update products set quantity=%s where itemname=%s;"
				data1 = (orders,item2)
				connection.execute(add1, data1)
				self.conn.commit()

				add2 = "insert into orders(name, datetime, amount) values(%s, %s, %s);"
				data = (item1, date, item3)
				connection.execute(add2, data)
				self.conn.commit()
				QMessageBox.about(self, "Added Successfully", "The Order/s was added Successfully")

				connection.execute("select name,datetime,amount from orders;")

				self.items_3.setRowCount(0)
				for row_number, row_data in enumerate(connection):
					self.items_3.insertRow(row_number)
					for colum_number, data in enumerate(row_data):
						self.items_3.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

				if orders == 0:
					outofstock.append(item2)

					connection = self.conn.cursor()
					add1 = "insert into outofstocks(itemname) values(%s);"
					data1 = (item2,)
					connection.execute(add1, data1)
					add2 = "delete from products where itemname=%s ;"
					data2 = (item2,)
					connection.execute(add2, data2)
					self.conn.commit()

					connection.execute("select itemname from outofstocks;")
					self.items_5.setRowCount(0)
					for row_number, row_data in enumerate(connection):
						self.items_5.insertRow(row_number)
						for colum_number, data in enumerate(row_data):
							self.items_5.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

					connection.execute("select itemname,quantity,price from products;")
					self.items.setRowCount(0)
					for row_number, row_data in enumerate(connection):
						self.items.insertRow(row_number)
						for colum_number, data in enumerate(row_data):
							self.items.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

					connection.execute("select itemname,quantity,price from products;")
					self.items_2.setRowCount(0)
					for row_number, row_data in enumerate(connection):
						self.items_2.insertRow(row_number)
						for colum_number, data in enumerate(row_data):
							self.items_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

	def payment(self):
		client = self.customername.text()
		money = self.paymentpaid_2.value()
		date = datetime.date.today()
		x = money
		change = 0
		for i in range(len(totalsss)):
			x -= totalsss[i]
			change = x

		if not self.orders:
			QMessageBox.warning(self,"Error","No orders yet")
			self.paymentpaid_2.setValue(0)

		elif int(money) < int(self.totals):
			QMessageBox.warning(self, "Error", "Insufficient money")

		else:
			prompt = QMessageBox.question(self, "NOTICE",
										  "Confirm Payment?",
										  QMessageBox.Yes | QMessageBox.No)
			self.amount.clear()
			self.paymentpaid_2.setValue(0)

			if prompt == QMessageBox.Yes:
				self.paymentpaid_3.setEnabled(True)
				self.reciepts.addItem('MY RECIPE BAKING SUPPLIES Co.')
				self.reciepts.addItem('(+63)9955598635')
				self.reciepts.addItem('Thank you ' + client + '!')
				self.reciepts.addItem('-------------------------------------')
				self.reciepts.addItem("Customer's Order:")
				for x in range(len(self.orders)):
					self.reciepts.addItem(self.orders[x])
				self.reciepts.addItem('-------------------------------------')
				self.reciepts.addItem('Money: P ' + str(money) + '0')
				self.reciepts.addItem('Change: P ' + str(change) + '0')
				self.reciepts.addItem('Thank you for ordering, Visit us again!')
				self.orders = []
				self.listoforder.clear()
				self.customername.clear()

				times = []
				timestamp = time.strftime('%H')
				times.append(int(timestamp))

				for x in range(len(times)):
					if times[x] >= 0:
						connection = self.conn.cursor()
						self.toalsales += self.totals
						a = self.toalsales

						check = "select * from totalsales where datetime=%s;"
						data = (date,)
						connection.execute(check, data)
						go = connection.fetchall()
						c = len(go)

						if c > 0:
							add = "update totalsales set totalsales=%s where datetime=%s;"
							data = (a, date)
							connection.execute(add, data)
							self.conn.commit()

							connection.execute("select datetime,totalsales from totalsales;")
							self.items_4.setRowCount(0)
							for row_number, row_data in enumerate(connection):
								self.items_4.insertRow(row_number)
								for colum_number, data in enumerate(row_data):
									self.items_4.setItem(row_number, colum_number,
														 QtWidgets.QTableWidgetItem(str(data)))

						else:
							add = "insert into totalsales(datetime, totalsales) values(%s, %s);"
							data = (date, a)
							connection.execute(add, data)
							self.conn.commit()

							connection.execute("select datetime,totalsales from totalsales;")
							self.items_4.setRowCount(0)
							for row_number, row_data in enumerate(connection):
								self.items_4.insertRow(row_number)
								for colum_number, data in enumerate(row_data):
									self.items_4.setItem(row_number, colum_number,
														 QtWidgets.QTableWidgetItem(str(data)))

					else:
						connection = self.conn.cursor()
						self.toalsales += self.totals
						a = self.toalsales

						check = "select * from totalsales where datetime=%s;"
						data = (date,)
						connection.execute(check, data)
						go = connection.fetchall()
						c = len(go)

						if c > 0:
							add = "update totalsales set totalsales=%s where datetime=%s;"
							data = (a,date)
							connection.execute(add, data)
							self.conn.commit()

							connection.execute("select datetime,totalsales from totalsales;")
							self.items_4.setRowCount(0)
							for row_number, row_data in enumerate(connection):
								self.items_4.insertRow(row_number)
								for colum_number, data in enumerate(row_data):
									self.items_4.setItem(row_number, colum_number,
														 QtWidgets.QTableWidgetItem(str(data)))
						else:
							add = "insert into totalsales(datetime, totalsales) values(%s, %s);"
							data = (date, a)
							connection.execute(add, data)
							self.conn.commit()

							connection.execute("select datetime,totalsales from totalsales;")
							self.items_4.setRowCount(0)
							for row_number, row_data in enumerate(connection):
								self.items_4.insertRow(row_number)
								for colum_number, data in enumerate(row_data):
									self.items_4.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
			else:
				pass

	def clear(self):
		self.amount.clear()
		self.reciepts.clear()

	# --------------------------------------------------------------------------------------------------------------#

	def adminadd(self):
		txt = self.Namesearch.text()
		quan = self.quanti.value()
		pri = self.doubleSpinBox_2.value()

		connection = self.conn.cursor()
		check = "select * from products where itemname=%s;"
		data = (txt,)
		connection.execute(check, data)
		go = connection.fetchall()
		c = len(go)
		if c > 0:
			a = "update products set quantity=%s,price=%s where itemname=%s;"
			dat = (quan,pri,txt)
			connection.execute(a, dat)
			self.conn.commit()
			self.Namesearch.clear()
			self.quanti.setValue(1)
			self.doubleSpinBox_2.setValue(1)

			for x in range(len(listahan)):
				if txt == listahan[x][0]:
					listahan[x][0] = txt
					listahan[x][1] = pri
					txt = listahan[x][0]
					pri = listahan[x][1]
					chk = x
					quants[chk] = quan
					quan = quants[chk]
				else:
					pass

			connection.execute("select itemname,quantity,price from products;")
			self.items.setRowCount(0)
			for row_number, row_data in enumerate(connection):
				self.items.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

			connections = self.conn.cursor()
			connections.execute("select itemname,quantity,price from products;")
			self.items_2.setRowCount(0)
			for row_number, row_data in enumerate(connections):
				self.items_2.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

		else:
			QMessageBox.warning(self, "Invalid Credentials", "Can't Read in the Database!")
			self.Namesearch.clear()


	def admindel(self):
		txt = self.Namesearch.text()

		connection = self.conn.cursor()
		check = "select * from products where itemname=%s;"
		data = (txt,)
		connection.execute(check, data)
		go = connection.fetchall()
		c = len(go)
		if c > 0:
			a = "delete from products where itemname=%s ;"
			dat1 = (txt,)
			connection.execute(a, dat1)
			b = "insert into outofstocks(itemname) values(%s);"
			dat2 = (txt,)
			connection.execute(b, dat2)
			self.conn.commit()
			self.Namesearch.clear()

			connection.execute("select itemname,quantity,price from products;")
			self.items.setRowCount(0)
			for row_number, row_data in enumerate(connection):
				self.items.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

			connection.execute("select itemname,quantity,price from products;")
			self.items_2.setRowCount(0)
			for row_number, row_data in enumerate(connection):
				self.items_2.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items_2.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))

			connection.execute("select itemname from outofstocks;")
			self.items_5.setRowCount(0)
			for row_number, row_data in enumerate(connection):
				self.items_5.insertRow(row_number)
				for colum_number, data in enumerate(row_data):
					self.items_5.setItem(row_number, colum_number, QtWidgets.QTableWidgetItem(str(data)))
		else:
			QMessageBox.warning(self, "Invalid Credentials", "Can't Read in the Database!")


	# --------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
	app = QApplication(sys.argv)
	iWindow = BS()
	iWindow.show()
	sys.exit(app.exec_())