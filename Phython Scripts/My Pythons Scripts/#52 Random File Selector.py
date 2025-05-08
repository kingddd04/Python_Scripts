# -*- coding: utf-8 -*-

# Importiamo i moduli os e random essenziali per il programma
import os
import random



# Questa funzione Prende in imput il path di una cartella e un estensione di un file e sceglie da essa
# Un percorso a caso  se è una cartella si esegue un altra volta se non trova niente restituisce un messaggio
def Random_File_Selector_From_Path(folderpath, extension):
    paths_in_folder = os.listdir(folderpath)   
    paths_dictionary = {number : path for number, path in enumerate(paths_in_folder)}
    random_file_index = random.randint(0, len(paths_dictionary)-1)
    fullpath = os.path.join(folderpath, paths_dictionary[random_file_index])
    if os.path.isdir(fullpath):
        res = Random_File_Selector_From_Path(fullpath, extension)
        return res
        
    elif fullpath.endswith(extension) and os.path.isfile(fullpath):
        return fullpath
    
        
#Funzione per stampare i risultati
def Print_Results(file_path):
    if file_path:
        file_Parts = file_path.split(os.sep)
        file_n = file_Parts[-1]
        print("\n" + "="*70)
        print("\t\t\t\tRESULTS")
        print("="*70)
        print()
        print(f"File Path: {file_path}")
        print()
        print(f"File Name: {file_n}")
        print("="*70)
    else:
        print("\n" + "="*70)
        print("\t\t\tRESULTS")
        print("="*70)
        print()
        print("-X- No file found with the specified extension.")
        print("="*70)

    
        
# Funzione Che gestisce l'interfaaccia utente gli errori  e il lancio del programma e il suo rilancio
def User_interface_And_Boot():
    
    # Con globals diciamo alla funzione che non vogliamo instanziare delle variabili locali ma fare riferimento
    #A delle Variabili Globali d'ora in poi quindi  previus_path e previus_extension modificheranno valori esterni alla 
    # Funzione
    global previus_path
    global previus_extension
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║                      Random_File_Selector                  ║
    ║                                                            ║
    ║   Welcome to the Random File Selector Tool! This tool can  ║
    ║   help you select a random file from a specified folder,   ║
    ║   including any subfolders. You can also specify a file    ║
    ║   extension (e.g., .txt, .pdf) to filter the files. If you ║
    ║   don't have any specific preferences, simply leave the    ║
    ║   field empty and press Enter.                             ║
    ║                                                            ║
    ║   Steps:                                                   ║
    ║   1. Provide a valid folder path. If you leave this field  ║
    ║      empty, the tool will analyze the current folder.      ║
    ║   2. (Optional) Specify a file extension. If you leave     ║
    ║      this field empty, all files will be considered.       ║
    ║                                                            ║
    ║   Note: Ensure you provide a valid folder path to avoid    ║
    ║   errors.                                                  ║
    ╚════════════════════════════════════════════════════════════╝
          """)
          
    print("\n\nEnter the file folder or leave empty to work on this folder: ")
    inp_path = input("---> ")
    if "exit" in inp_path:
        print("\n--You are exiting from the program--\n")
        return
    
    if "\"" in inp_path:
        inp_path= inp_path.replace("\"", "")
        
    if inp_path == "p":
        inp_path = previus_path
    
    print("\n\nEnter the file extension (e.g., .txt, .pdf) or leave empty for any file: ")
    inp_ext = input("---> ")
    if "exit" in inp_ext:
        print("\n--You are exiting from the program--\n")
        return
    
    if inp_ext == "p" :
        inp_ext = previus_extension
    
        
    
    if not inp_path: 
        inp_path = os.getcwd() # Use the current working directory if no path is provided
    if not inp_ext:
        inp_ext = ""
    if not os.path.isdir(inp_path):
        print("\n-X- The provided path is not a valid directory. Try again\n")
        User_interface_And_Boot()
    
    previus_path, previus_extension = inp_path, inp_ext
    Random_File_Path = Random_File_Selector_From_Path(inp_path, inp_ext)
    Print_Results(Random_File_Path)
    User_interface_And_Boot()
    return
    
        
    
previus_path, previus_extension = "", ""
User_interface_And_Boot()

#print(random.randint(0, 3))
        