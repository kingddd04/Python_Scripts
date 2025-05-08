"""
[number of functions_written, number of rows_of_code_written]
"""


import os

    
    

def Recursive_explorer_Booter(fol_p):
    current_folder = "C:\\Users\\david\\OneDrive\\Documents\\Phython Scripts" # os.path.getcwd
    Res = Recursive_explorer(current_folder, [0,0])
    return Res
    
def Py_Code_Explorer(fileparh):
    row_Counter = 0
    def_count = 0
    try:
        with open(fileparh, "r", encoding="utf-8") as txt:
            txt_lines = txt.readlines()
            for line in txt_lines :
                if len(line) > 3:
                    row_Counter+= 1
                if "def" in line:
                    def_count+=1
    except UnicodeDecodeError:
        pass
    
    return row_Counter, def_count
    
        
        
def Recursive_explorer(folder_path, results):
    for path in os.listdir(folder_path):
        fullpath = folder_path+"/"+ path
        if os.path.isfile(fullpath):
            row_c , def_c = Py_Code_Explorer(fullpath)
            if row_c != 0 and def_c != 0:
                results[0]+= row_c
                results[1]+= def_c
    for path in os.listdir(folder_path):
        fullpath = folder_path+"/"+ path
        if os.path.isdir(fullpath):
            Recursive_explorer(fullpath, results)
    return results


def write_results(results):
    row_Counter, def_count = results
    print("╔════════════════════════════════════╗")
    print("║    Your python stats:              ║")
    print("╠════════════════════════════════════╣")
    print("║ Total lines of code typed:"+str(row_Counter))
    print("║ Number of functions created:"+str(def_count))
    print("╠════════════════════════════════════╣")
    print("║     Keep on coding and have fun!   ║")
    print("╚════════════════════════════════════╝")


results = Recursive_explorer_Booter("y")
write_results(results)



            
            
            
            
            

        
        
    
    
        
    