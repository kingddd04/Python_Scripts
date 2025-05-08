#Questa Funzione è ricorsiva ovvero chiama se stessa e si autoesegue fino a quando non sarà raggiunto il caso base.
#Il caso Base è quella condizione che anzichè riavviare il processo di ricorsione (la funzione che chiama se stessa)
#Lo Termina restituendo tramite return un elemento definito che non va ricavato con altre chiamate.


#Come Vediamo Dallo script Il modo di risolvere questo tipo di esercizi è creare un problema più piccolo
#Che si autorisolve da se tramite un evoluzione lineare, logica e armonica

#Funz.Ric prende in input un numero che progressivamente viene abbassato fino a quando non è uguale a 0
def factorial_raiser(n):
    # print(n)
    if n == 0:                             #Se il caso base viene raggiunto viene restituito 1 e viene fermata la ricorsiome
        return 1                           # Ecco il caso base, ovvero lo stop alla ricorsione
    else:                                  # Se il caso base non è raggiunto la funzione viene rinvocata tuttavia diminuenddo n di 1
        return n * factorial_raiser(n - 1) #Ecco qui la nostra chiamata ricorsiva che verrà rieseguita fino a quando sarà raggiunto il caso base
    
    
    
    
#Perchè funziona? Come le matriosche le ricorsioni si annidano l'una dentro l'altra
# Esempio in Factorial_raiser(3) n != 0 quindi si richiede 3 * Factorial_raiser(2)
# e ancora n != 0 e quindi si richiede 2* Factorial_raiser(1) e ancora n != 0
# Quindi si richiede 1*Factorial_raiser(0), che restituisce 1 perchè n è 0 le chiamate 
#Sono state interrotte e quindi ora la ricorsione svolgera i calcoli richiesti, ovvero farà
#1*1*2*3*4 risolvendo prima la chiamata più profonda poi quella iniziale
               
               
             
#Interfaccia utente
    
print("\n---Calcolatore Fattoriale Ricorsivo---")
print("""
      Questo codice usa l'elegante e efficiente metodo ricorsivo 
      per calcolare il fattoriale di un numero intero, inserisci un numero e prova!
      """)
      
int_imput = input("Inserisci qui solo il numero (non altro!) del quale vuoi calcolare il fattoriale n! : ")
if int_imput.isdigit():
    print("")
    numb = int(int_imput)
    Result = factorial_raiser(numb)
    print("- - - - -  - - - - - - - - - - - - - - - - - - - - - -\n")
    print("Ecco il risultato della tua operazione : "+ str(Result))
else:
    print("\nQuale parte di inserisci solo il tuo numero non ti è chiara?\nRiavvia il programma!\n")