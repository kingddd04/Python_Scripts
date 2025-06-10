inp_number = input("Insert you number here!    -  ")

if inp_number.isdigit():
	int_input_numb = int(inp_number)
	if int_input_numb // 2 == 0 and int_input_numb % 2 == 0:
		print("\n\n YOUR NUMBER IS ODD")
	else:
		print("\n\n YOUR NUMBER IS EVEN")
else:
	raise TypeError ("Insert A Valid Number")