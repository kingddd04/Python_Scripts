def strong_pseudo_random(seed: int, v1: int, v2: int) -> int:
    # Costanti prime ottimizzate per la dispersione dei bit
    A = 2654435761  # Knuth's multiplicative constant
    B = 2246822519
    C = 3266489917


    # Combinazione iniziale dei valori
    combined = (seed * A) ^ (v1 * B) ^ (v2 * C)

    # Mixing aggressivo (ispirato a MurmurHash3)
    combined ^= (combined >> 16)
    combined = (combined * 0x85ebca6b) & 0xFFFFFFFF  # masking a 32 bit
    combined ^= (combined >> 13)
    combined = (combined * 0xc2b2ae35) & 0xFFFFFFFF
    combined ^= (combined >> 16)

    # Generazione del numero finale tra 1 e 100
    random_number = (abs(combined) % 100) + 1

    return random_number

for i in range(20, 520, 20):
    #print(i)
    print(strong_pseudo_random(123456789, 1, i), end=" , ")  # Esempio di utilizzo