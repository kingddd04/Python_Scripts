letter = input("insert letter!")

cons = "qwrtypsdfghjklzxcvnbm"
voc = "eioua"

if len(lower_l) == 1:
	lower_l = letter.lower()

	if lower_l in cons:
		print("Consonant")

	if lower_l in voc:
		print("vocal")