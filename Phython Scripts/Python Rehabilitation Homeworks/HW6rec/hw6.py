# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 19:20:33 2024

@author: user
"""

# -*- coding: utf-8 -*-
from pngmatrix import load_png8

def ex(file_png, file_txt, file_out):
    Matrix = load_png8(file_png)
    #print (Matrix)
    # Calcolare il numero di righe e colonne
    numero_di_righe = len(Matrix)
    numero_di_colonne = len(Matrix[0])  # Assumendo che tutte le righe abbiano la stessa lunghezza
    return Matrix

def trova_quadrati_rettangoli_colorati(Matrix):
    quadrati_rettangoli = []

    for riga in range(len(Matrix)):
        for colonna in range(len(Matrix[0])):
            colore_corrente = Matrix[riga][colonna]

            # Verifica se il colore è diverso da nero (assumendo che il nero sia rappresentato come [0, 0, 0])
            if colore_corrente != (0, 0, 0):
                inizio_riga, inizio_colonna, fine_riga, fine_colonna = trova_dimensioni_rettangolo(Matrix, riga, colonna, colore_corrente)
                altezza = fine_riga - inizio_riga + 1
                larghezza = fine_colonna - inizio_colonna + 1

                quadrati_rettangoli.append({
                    'colore': colore_corrente,
                    'inizio': (inizio_riga, inizio_colonna),
                    'fine': (fine_riga, fine_colonna),
                    'altezza': altezza,
                    'larghezza': larghezza
                })

                # Imposta a nero la regione esaminata per evitare doppie contabilizzazioni
                for i in range(inizio_riga, fine_riga + 1):
                    for j in range(inizio_colonna, fine_colonna + 1):
                        Matrix[i][j] = (0, 0, 0)

    return quadrati_rettangoli

def trova_dimensioni_rettangolo(Matrix, riga, colonna, colore_corrente):
    inizio_riga, inizio_colonna, fine_riga, fine_colonna = riga, colonna, riga, colonna

    # Trova fine_riga
    while fine_riga < len(Matrix) and Matrix[fine_riga][colonna] == colore_corrente:
        fine_riga += 1

    # Trova fine_colonna
    while fine_colonna < len(Matrix[0]) and Matrix[riga][fine_colonna] == colore_corrente:
        fine_colonna += 1

    return inizio_riga, inizio_colonna, fine_riga - 1, fine_colonna - 1


Matrix=ex("image1.png", 677, 778)
quadrati_rettangoli_trovati = trova_quadrati_rettangoli_colorati(Matrix)

for figura in quadrati_rettangoli_trovati:
    colore = figura['colore']
    inizio = figura['inizio']
    fine = figura['fine']
    altezza = figura['altezza']
    larghezza = figura['larghezza']
    print(f"Colore: {colore}, Inizio: {inizio}, Fine: {fine}, Altezza: {altezza}, Larghezza: {larghezza}")
