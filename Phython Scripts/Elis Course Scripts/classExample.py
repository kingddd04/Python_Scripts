class Automobile: 
	def __init__(self, marca, modello , cilindrata):
		self.marca = marca
		self.modello = modello
		self.cilindrata = cilindrata

	def stampaAttributi(self):
		print(f"Marca {self.marca}")
		print(f"Marca {self.modello}")
		print(f"Marca {self.cilindrata}")


def main():
	macchina1 = Automobile("Citroen", "C5", 1008)
	macchina1.stampaAttributi()


main()