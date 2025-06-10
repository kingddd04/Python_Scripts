valid_numbers = 0

numbers_container = [0,0,0]

while valid_numbers != 3:
	input_int = input(f"\ninsert the {valid_numbers+1} number _ _ _  ")
	try:
		n = int(input_int)
		if n not in numbers_container:
			valid_numbers += 1
			numbers_container[valid_numbers-1] = n 
		else:
			print("\nYou cannot insert the same number! ")
	except ValueError: 
		print("\nInsert a valid number! ")
		continue


numbers_container.sort()
print("Higher number is : " + str(numbers_container[2]))
print("Lower number is : " + str(numbers_container[0]))

