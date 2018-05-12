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

def getInput():
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
		#Todo: integrate invoice creation method
                print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
                userInput = getInput()

	elif(userInput==2):
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
		print("\n1 - Query by customer last name\n2 - Query by charge type\n3 - View all outstanding invoices\n")
		queryChoice = getInput()
		if(queryChoice == 0):
                        print("Back")
		elif(queryChoice == 1):
                        query = str(input("Input last name: "))
                        query = query.upper()

                        for name in db.Invoices.find({"Last name" : query}):
                                pprint.pprint(name)
                                print("-------------------------------------------------------------------------------------")

		elif(queryChoice == 2):
                        query = str(input("Input charge type: "))
                        query = query.upper()

                        for invoice in db.Invoices.find({"Items": query}):
                                pprint.pprint(invoice)
                                print("-------------------------------------------------------------------------------------")

		elif(queryChoice == 3):
                        for invoice in db.Invoices.find():
                                pprint.pprint(invoice)
                                print("-------------------------------------------------------------------------------------")

		else:
                        print("Invalid input")

		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()
	
	elif(userInput==4):
		userFName = str(input("Input first name: "))
		userLName = str(input("Input last name: "))
		userEmail = str(input("Input Email: "))
		userNum = str(input("Input phone number: "))
		userDict = {
			"First Name": userFName,
			"Last Name": userLName,
			"Email": userEmail,
			"Phone Number": userNum
		}
		docID = db.Users.insert_one(userDict).inserted_id
		print("\nUser added:\n")
		pprint.pprint(db.Users.find_one({"_id": docID}))
		
		print("\n1 - Generate new invoice\n2 - View users\n3 - View outstanding invoices\n4 - Generate new user\n5 - View archived invoices\n")
		userInput = getInput()
		
	elif(userInput==5):
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
