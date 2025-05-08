import os.path
    
def Messages(Mess_id):
    if Mess_id == 0:
        print("""
             Simple Text File Password Manager
            
        This simple text editor can help you to create and edit
        A file to keep all your passwords in one place
             """)
    if Mess_id == 1:
        print("""
        Instructons: type the following commands to select or createthe file the program
        will edit and use       
                            newfile : Create a new file 
                            loadfile : Select the existing file to be edited
                            exit : Exit from the program
              """)
    if Mess_id == 2:
        print("""
              --------------------------
              You successfully exited from Simple Text File Password Manager
              --------------------------
              """)
    
    if Mess_id == 3:
        print("""
              Paste your full path to th file Here !! ("" are allowed there is no need to delete them:) )         
              """)
    if Mess_id == 4:
        print("""
               Paste Here the path where you want your file to be created you can include ("")
               You can type currfold to select the folder where this file is executed
               """)
    if Mess_id == 5:
        print("""
              Insert Here your File name And extension like this, example.txt
              """)
    if Mess_id == 6:
        print("""
        Select the operation for your File!
            addpass : Adds a password to your text file
            editpass : Edits an existing password row
            sortpass : Sorts all passwords in your file
            delpass : Deletes a password from your text file 
            exit : Exit from the program
              """)
    if Mess_id == 7:
        print("""
              Insert The Usage place of the password, the site, the device ecc..
              """)
    if Mess_id == 8:
        print("""
              Insert The Username for your site
              """)
    if Mess_id == 9:
        print("""
              Insert The Password
              """)
    if Mess_id == 10:
        print("""
              Insert Today date (dd/mm/yyyy) example(07/05/2004)
              """)
    if  Mess_id == 11:
        print("""
              Your Imput Has generated an error !! Please try again
              """)
    return
        
def Add_Password(filepath):
    Messages(7)
    Name = input("\n. . . ")
    Messages(8)
    Username = input("\n. . . ")
    Messages(9)
    Password = input("\n. . . ")
    Date = input("\n. . . ")
    if len(Name) < 32 or len(Password) < 32:
        spaces_to_add = 48-len(Name)
        string = Name+" Username: "+ Username + " "*spaces_to_add +" Password: "+ Password
        with open(filepath,"a") as file:
            file.write(string)     
    Menu2(filepath)
        
def print_pass(lines):
    count_l = 0
    for line in lines:
        print(str(count_l)+ " = " +line[0,64] +"...\n")  
    return

def Remove_Password(filepath):
    with open(filepath,"r", encoding="utf8") as txt:
        lines = txt.readlines()
    print_pass(lines)
    row_index = input("\n. . . ")
    if "exit" in row_index:
        Menu2(filepath)
    try:
         removed_i = lines.pop(int(input()))
         print("\nRemoved Item : "+removed_i+"\n")
         with open(filepath,"w",encoding="utf8") as sus:
             sus.writelines(lines)
    except Exception as e:
        Remove_Password(filepath)
    return   
        
    

def Sort_Password():
    pass
def Edit_Password():
    pass

def Elaborate_File_Path(filepath):
    if "" in filepath:
        filepath.replace("\"", "")
    return filepath

def Menu_1():
    Messages(0)
    Messages(1)
    new_or_Load = input("\n. . . ")
    if "newfile" in new_or_Load:
        Messages(4)
        new_path_raw = input("\n. . . ")
        if "currfold" in new_path_raw:
            new_path_raw = os.getcwd()
        new_path = Elaborate_File_Path(new_path_raw)
        Messages(5)
        filename = input("\n. . . ")
        fullpath = new_path + "\\" +  filename
        return fullpath
    
    elif "loadfile" in new_or_Load:
        Messages(3)
        RawFilepath = input("\n. . . ")
        Good_Path = Elaborate_File_Path(RawFilepath)
        return Good_Path
    elif "exit":
        pass
    else:
        Messages(6)
        Menu_1()
    return

def Menu2(filepath):
    Messages(6)
    Command_select = input("\n. . . ")
    if "addpass" in Command_select:
        Add_Password(filepath)
    elif "editpass" in Command_select:
        Edit_Password()
    elif "delpass":
        Remove_Password()
    elif "sortpass":
        Sort_Password()
    elif "exit":
        pass
    else:
        Menu2(filepath)
    return
      
def Manager():
    filepath = Menu_1()
    Menu2(filepath)

Manager()
  
    
