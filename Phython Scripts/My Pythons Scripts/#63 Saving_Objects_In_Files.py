""" 
In this script we will understand how to save objects in files, dekete them and load them back.
We also citate a static method to load the object from the file.
A static method is a method that belongs to the class rather than an instance of the class.
And does not require an instance of the class to be called.
"""


import pickle
import os   

class NotePad:
    def __init__ (self, title, author, date , content): # Constructor to initialize the notepad object
        self.title = title
        self.author = author
        self.date = date
        self.content = content
        
        
    def save_to_file(self, filename):
        local_path = os.getcwd()  # Get the current working directory
        full_path = local_path + "\\Test Material\\" + filename + ".plk"  # Create the full path for the file
        with open(full_path, "wb") as file:
            pickle.dump(self, file)
            print(f"\n\nNotepad saved to {full_path}")

    @staticmethod # Static method to load the notepad from a file without needing an instance
    def load_from_file(filename):
        local_path = os.getcwd()  # Get the current working directory
        full_path = local_path + "\\Test Material\\" + filename + ".plk"  # Create the full path for the file
        with open(full_path, "rb") as file:
            notepad = pickle.load(file)
            return notepad
        
    def print_notepad(self): # Method to print the notepad details
        print(f"Title: {self.title}")
        print(f"\nAuthor: {self.author}")
        print(f"\nDate: {self.date}")
        print(f"\nContent: {self.content}")
        print("\n\n")
    
    
def main():
    notepad = NotePad("My First Note", "John Doe", "2023-10-01", "This is the content of my first note.")
    notepad.save_to_file("notepad1") # Save the notepad to a file
    
    del notepad  # Delete the notepad object to demonstrate loading from file
    
    notepad1 = NotePad.load_from_file("notepad1") # Load the notepad from the file
    notepad1.print_notepad()
    

if __name__ == "__main__":
    main()