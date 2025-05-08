import os 

#This method getcwd returns the path of the current folder
current_folder = os.getcwd()
print("Now we are scanning : "+current_folder)
# This Method Returns the list of all the names in the current directory
# We Can iterate throught it and scan all paths
for nome in os.listdir(current_folder):
    print("\n"+ nome)
    #let's get the full filepath string
    fullname = current_folder+"/"+nome
    # .isfile(filepath) detects if the path is a file 
    if os.path.isfile(fullname):
        print("-This One is a File\n")
        #.endswith is used here to check the file extension 
        if fullname.endswith(".txt"):
            print("-This is a text file!")
        if fullname.endswith(".py"):
            print("-This is a python program!")
        if fullname.endswith(".png"):
            print("-This file is a png image!")
    #.isdir(filepath) detect if the current filepath is a folder
    elif os.path.isdir(fullname):
        print("-This One is a folder")
    else:
        print("error? what is this?\n")
