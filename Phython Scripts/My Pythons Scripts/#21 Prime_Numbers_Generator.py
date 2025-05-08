#L'Algoritmo di Questo Programma è stato creato da chatgtp Io ho creato 
#Solo L'interfaccia utente
print("""
|---Generatore Di Numeri Primi---\
    
      """)

n_input = input("Inserisci il numero fino al quale vuoi trovare tutti i numeri primi :  ")

print("\n------\n")

def GeneratoreNumeriPrimi(n):
    numeri = list(range(2, n + 1))
    numeri_primi = []

    while numeri:
        primo = numeri[0]
        numeri_primi.append(primo)
        numeri = [x for x in numeri if x % primo != 0]

    return numeri_primi

Result = GeneratoreNumeriPrimi(int(n_input))
print("")
print(Result)
print("\n------")
