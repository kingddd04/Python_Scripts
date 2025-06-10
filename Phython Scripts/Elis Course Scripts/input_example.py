eta = 29
citta = "Roma"

stringa_input = input("Inserisci il tuo nome! ")


def stampasaluto(eta,citta,saluto= "Ciao ",):
	print(saluto + stringa_input, end = " ,")
	print(" vieni da : "+ citta, end=" ,")
	print(" hai  "+ str(eta) + " anni ", end=" ,")
	return "\n\nHo salutato l'utente !"

#sottostringa = stringa_input[0:len(stringa_input):3]

print(stampasaluto(eta, citta ))
print(stampasaluto(eta, citta ))