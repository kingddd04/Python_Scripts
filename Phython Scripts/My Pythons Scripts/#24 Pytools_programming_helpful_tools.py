# -*- coding: utf-8 -*-
import sys

sys.path.append(r'C:\Users\david\OneDrive\Documents\Phython Scripts\My Pythons Scripts\Libraries')

from pngmatrix import load_png8
from pngmatrix import save_png8

keep_alive = True

def Item_Counter(item_counter):
    counter = 0
    Variable_creator = eval(item_counter)
    for item in Variable_creator:
        counter +=1
    output = "\n---"+str(counter)+"---\n"
    return output


while keep_alive == True:
    
    
    print("""
    ---Python tools---
    
    This set of tools can help you in varius ways while coding
    
    Tools list:
        1: List counter, count the number of items in your list, sting ecc...
        2: Images To Matrix converter the script returns a list of list of tuples
        "exit": exit from Python Tools
        3:Matrix counter given a Matrix indicate the number 
        4: Replace char, replace any character with another replace
        5: Image From Matrix, allows you create a new .png image from a raw matrix of tuples RGB
        
        
        """)
    Py_tools_select=input("Type the number of the tool you want to use-->> ")
    
    if "1" in Py_tools_select:
        item_counter = input("\nInsert the list/list of tuple ecc.. that you wanna count > ")
        print(Item_Counter(item_counter))
        stop_it = input("press enter to continue _ ")
        
    if "2" in Py_tools_select:
        Filepath = input("\nInsert the full file path of the image that you wanna convert in a Matrix(exclude \"\" please) > ")
        print("")
        Matrix = load_png8(Filepath)
        print(Matrix)
        stop_it = input("press enter to continue _ ")
    
    if "3" in Py_tools_select:
        Matrix_input = input("Insert the matrix you want to know the number of rows (x) and the number of columns (y) : ")
        Matrix = eval((Matrix_input))
        n_row_x = len(Matrix)
        n_columns_y = len(Matrix[0])
        n_x = n_row_x - 1
        n_y = n_columns_y - 1
        print("\nYour Matrix has "+ str(n_x)+" rows (x) and "+ str(n_y)+" columns y\n")
        stop_it = input("press enter to continue _ ")
        
    
    if "4" in Py_tools_select:
        Str_input = input("\nInsert here the text you want to elaborate :")
        Char_to_be_replaced = input("\nInsert the character/consecutive characters you want to be replaced in the text :")
        Char_to_replace = input("\nInsert the char you want to replace in the text(insert nothing to delete the character) :")
        Elaborated_Text = Str_input.replace(Char_to_be_replaced, Char_to_replace)
        print("\nYour Output text : \n"+Elaborated_Text)
        stop_it = input("press enter to continue _ ")
        
    if "5" in Py_tools_select:
        Str_Matrix = input("\n-Please paste here your matrix -> ")
        Matrix = eval(Str_Matrix)
        print("\n-Good! Your image will be created in the current folder now add a name for the file remeber to add . png in the end!\n")
        Str_input = input("\n-Insert here your file name (add .png in the end:)")
        save_png8(Matrix,Str_input)
        print("\n-Your image was created in this folder!")
        
    if "6" in Py_tools_select:
        
        

        
    
    if "exit" in  Py_tools_select:
        keep_alive = False
        print("""
        ---You are exiting from Python Tools, have a good coding day!---
              """)