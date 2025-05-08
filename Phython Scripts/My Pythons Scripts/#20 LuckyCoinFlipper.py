keep_playing = True   
while keep_playing == True:
    
    import random
    print("---CoinFlipper, Coraggio lancia Una Moneta!---\n")
    CoinValue = random.randint(1, 100)
    CoinValueWin = 50
    Ready4Launch = input("Premi invio per lanciare! Oppure scrivi esc per uscire!  >>> ")
    if "esc" in Ready4Launch:
        print("\nArrivederci! Speriamo che la buona sorte ti sia sempre amica!\n")
        keep_playing = False
        print("Ultimo lancio Fortunato!\n")
    if CoinValue >= CoinValueWin :
        print("\nE'Uscita Testa!\n")
    elif CoinValue < CoinValueWin:
        print("\nE'Uscita Croce\n")
    print("-------------\n")
     