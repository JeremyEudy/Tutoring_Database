#Author: Jeremy Eudy
#Usage: python3 CLIFrontEnd.py
import pymongo
from pymongo import MongoClient
import sys
import gridfs
import pprint

client = MongoClient()
db = client.Tutoring_Database

print("Welcome to the Tutoring Invoice Database")
print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")

def getInput(): #Simple input reciever
        while (True):
                try:
                        userInput = int(input("Please input a choice (0 to exit): "))
                except ValueError:
                        print("Please enter a valid integer")
                else:
                        return userInput

userInput = getInput()

while(True):
	if(userInput == 0):
		sys.exit()
	
	elif(userInput==1):
		print("\nInvoice service code reference:\nST - Standard Tutoring - 45 minutes - $35\nST Staff - Standard Tutoring - 45 minutes, CCHS staff rate - $30\nST 1Hr - Standard Tutoring - 1 hour - $45\nST 1Hr Staff - Standard Tutoring - 1 hour, CCHS staff rate - $40\nADV - Advanced Tutoring - 45 minutes AP, DC, College or Calculus Honors - $40\nADV Staff - Advanced Tutoring - 45 minutes AP, DC, College or Calculus Honors, CCHS staff rate - $35\nADV 1Hr - Advanced Tutoring - 1 hour AP, DC, College or Calculus Honors - $50\nADV 1Hr Staff - Advanced Tutoring - 1 hour AP, DC, College or Calculus Honors, CCHS staff rate - $45\nSAT/ACT - SAT/ACT math tutoring - 45 minutes - $40\nSAT/ACT Staff - SAT/ACT math tutoring - 45 minutes, CCHS staff rate - $35\nSAT/ACT 1Hr - SAT/ACT math tutoring - 1 hour - $50\nSAT/ACT 1Hr Staff - SAT/ACT math tutoring - 1 hour, CCHS staff rate - $45\nAP - AP Math Tutoring - 1 hour - $60\n Credit - Custom item package, price varies.")
				
		invDate = str(input("Enter invoice issue date: "))
		invEmail = str(input("Enter client email: "))
		
		#Get existing user information from user database
		for user in db.Users.find({"Email" : invEmail}):
			invFName = user["First Name"]
			invLName = user["Last Name"]
			invS1 = user["Student 1"]
			if(user["Student 2"] != "N/A"):
				invS2 = user["Student 2"]
			if(user["Student 3"] != "N/A"):
				invS3 = user["Student 3"]
			if(user["Student 4"] != "N/A"):
				invS4 = user["Student 4"]
		
		#Assign student information if it exists
		invName = invFName + " " + invLName
		invCode1 = str(input("Enter student 1 service code: "))
		if 'invS2' in locals():
			invCode2 = str(input("Enter student 2 service code: "))
		if 'invS3' in locals():
			invCode3 = str(input("Enter student 3 service code: "))
		if 'invS4' in locals():
			invCode4 = str(input("Enter student 4 service code: "))
		
		#Declaration currently broken since idk appropriate dictionary logic
		#invDict = {
		#	"Issue Date" : invDate,
		#	"Client Name" : invName,
		#	"Client Email" : invEmail,
		#	"Student 1 Name" : invS1,
		#	"Student 1 Code" : invCode1,
		#	"Student 2 Name" : invS2 if 'invS2' in locals(),
		#	"Student 2 Code" : invCode2 if 'invS2' in locals(),
		#	"Student 3 Name" : invS3 if 'invS3' in locals(),
		#	"Student 3 Code" : invCode3 if 'invS3' in locals(),
		#	"Student 4 Name" : invS4 if 'invS4' in locals(),
		#	"Student 4 Code" : invCode4 if 'invS4' in locals()
		#}

		#docID = db.Invoices.insert_one(invDict).inserted_id
		#print("\nInvoice data added:\n")
		#pprint.pprint(db.Invoices.find_one({"_id": docID}))		

		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()

	elif(userInput==2):
		#Cannibalized code from SGA_Database
		print("\n1 - Query by last name\n2 - View all users")
		queryChoice = getInput()
		if(queryChoice == 0):
			print("Back")
		elif(queryChoice == 1):
			query = str(input("Input last name: "))
			query = query.upper()
			
			for name in db.Users.find({"Last name" : query}):
				pprint.pprint(name)
				print("-------------------------------------------------------------------------------------")
		
		elif(queryChoice == 2):
			for x in db.Users.find():
				pprint.pprint(x)
				print("-------------------------------------------------------------------------------------")
		
		else:
			print("Invalid input")
		
		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()

	elif(userInput==3):
		print("\n1 - View outstanding balance\n2 - Query by customer last name\n3 - Query by charge type\n4 - View all outstanding invoices\n")
		queryChoice = getInput()
		if(queryChoice == 0):
                        print("Back")
		elif(queryChoice == 1):
			#Checks through entire collection and adds "Total" fields together to generate outstanding balance
			balance = 0
			for invoice in db.Invoices.find({},{ "_id" : 0,  "Total": 1 }):
				balance += int(invoice["Total"])
			print("The current outstanding balance is:", balance)
		elif(queryChoice == 2):
                        query = str(input("Input last name: "))
                        query = query.upper()

                        for name in db.Invoices.find({"Last name" : query}):
                                pprint.pprint(name)
                                print("-------------------------------------------------------------------------------------")

		elif(queryChoice == 3):
                        query = str(input("Input charge type: "))
                        query = query.upper()

                        for invoice in db.Invoices.find({"Items": query}):
                                pprint.pprint(invoice)
                                print("-------------------------------------------------------------------------------------")

		elif(queryChoice == 4):
                        for invoice in db.Invoices.find():
                                pprint.pprint(invoice)
                                print("-------------------------------------------------------------------------------------")

		else:
                        print("Invalid input")

		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()
	
	elif(userInput==4):
		#Form to generate new users
		userFName = str(input("Input first name: ")).upper()
		userLName = str(input("Input last name: ")).upper()
		userEmail = str(input("Input Email: ")).upper()
		userNum = str(input("Input phone number: "))
		student1 = str(input("Input student 1 name: ")).upper()
		student2 = str(input("Input student 2 name (or N/A): ")).upper()
		student3 = str(input("Input student 3 name (or N/A): ")).upper()
		student4 = str(input("Input student 4 name (or N/A): ")).upper()
		userDict = {
			"First Name": userFName,
			"Last Name": userLName,
			"Email": userEmail,
			"Phone Number": userNum
			"Student 1" = student1
			"Student 2" = student2
			"Student 3" = student3
			"Student 4" = student4
		}
		docID = db.Users.insert_one(userDict).inserted_id
		print("\nUser added:\n")
		pprint.pprint(db.Users.find_one({"_id": docID}))
		
		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()
		
	elif(userInput==5):
		#Useless until InvoiceUpload.pl is fixed
		print("\n1 - Query by customer last name\n2 - Query by charge type\n3 - View all archived invoices\n")
		queryChoice = getInput()
		if(queryChoice == 0):
			print("Back")
		elif(queryChoice == 1):
			query = str(input("Input last name: "))
			query = query.upper()
			
			for name in db.ArchivedInvoices.find({"Last name" : query}):
				pprint.pprint(name)
				print("-------------------------------------------------------------------------------------")
		
		elif(queryChoice == 2):
			query = str(input("Input charge type: "))
			query = query.upper()
			
			for invoice in db.ArchivedInvoices.find({"Items": query}):
				pprint.pprint(invoice)
				print("-------------------------------------------------------------------------------------")
		
		elif(queryChoice == 3):
			for invoice in db.ArchivedInvoices.find():
				pprint.pprint(invoice)
				print("-------------------------------------------------------------------------------------")
		
		else:
			print("Invalid input")
		
		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()

	else:
		print("Invalid Input")
		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()
