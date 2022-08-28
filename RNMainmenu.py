def showMenu(resMenu):
	if(resMenu == 1):
		print("\n\n*********RN College Candidate Menu*********\n \n")
		print("Press 1 for Create application Registration ")
		print("Press 2 for View available courses ")
		print("Press 3 for Viewing the Candidate application ")
		print("Press 4 for Updating the Candidate application ")
		print("Press 9 to Go back to main menu ")
		print("Press 0 to exit menu \n")


	else:
		print("\n\n*********RN College Administration Menu*********\n \n")

		print("Press 1 for Viewing the Candidate application ")
		print("Press 2 for View available courses ")
		print("Press 3 for Update the Courses ")
		print("Press 4 for Updating the Candidate application ")
		print("Press 9 to Go back to main menu ")
		print("Press 0 to exit menu \n")		
	
	return int(input("Enter Your response - "))

mainResponse = 1
while(mainResponse != 0):
	print("\n\n******RN College Main Menu******\n \n")
	print("Press 1 for Candidate Menu")
	print("Press 2 for Adminstration Menu")
	print("Press 0 to exit menu \n")

	mainResponse = int(input("Enter Your response - "))
	#print("the response ",mainResponse)
	if(mainResponse < 3):
		resMenu = showMenu(mainResponse)
	else:
		print("******* Please enter a VALID Response *****")

print(" Thanks for using RN College Application - Good Bye ")
