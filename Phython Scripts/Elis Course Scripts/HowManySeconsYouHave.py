
try:
	#Isdigit could be also used
	user_age = int(input("Insert Your Age here ! - "))
	print("You have : "+ str(user_age * 12) + " months")
	print("You have : "+ str(user_age * 365) + " days")
	print("You have : "+ str(user_age * 365*24)+ " hours")
	print("You have : "+ str(user_age * 365*24*60)+ " seconds")
	print("You have : "+ str(user_age * 365*24*60*1000)+ " millisecods")



except ValueError:
	raise ValueError ("Insert a valid number you fool")
