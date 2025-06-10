inp_number = input("Insert you number here!    -  ")

if inp_number.isdigit():
	int_input_numb = int(inp_number)
	if int_input_numb >= 18:
		print("You have reached mayor age")
	if int_input_numb < 18:
		print("You have still not reached the mayor age")
	if int_input_numb > 20 and int_input_numb < 30 :
		print("\n\n You are very young!")
	elif int_input_numb > 31 and int_input_numb < 50:
		print("\n\n You are starting to be old")
	else:
		print("\n\n You look no more so young ")
else:
	raise TypeError ("Insert A Valid Number")