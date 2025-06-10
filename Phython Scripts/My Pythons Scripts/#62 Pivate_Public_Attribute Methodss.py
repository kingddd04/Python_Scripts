""" 
Example of Private and Public Attributes and methods in Python Classes

This script demonstrates the use of private and public attributes in Python classes.
We have a object with a private attribute and a public method to access it.
And another object with a public attribute that is not private that can be accessed from anywhere.
"""

class Vault:
    def __init__ (self):
        self.__secret_Phrase = "The Molise does not exist" # Private attribute not accessible outside the class
        self.__key = "Open Sesame" # Private attribute not accessible outside the class
        
    def __get_Secret_Phrase(self): # Private method to get the secret phrase not accessible outside the class
        return self.__secret_Phrase
    
    def vault_Lock(self, imput_Key): # Method to check the key and return the secret phrase if correct
        if imput_Key == self.__key:
            secret_phrase = self.__get_Secret_Phrase() # Call the private method to get the secret phrase
            return f"Vault Unlocked! Secret Phrase: {secret_phrase}"
        else:
            return "Access Denied"
        
        
class UnsafeVault(): # This class has a public attribute that can be accessed from  anywhere not safe
    def __init__(self):
        self.secret_Phrase = "Scampia is inabitable" # Public attribute
    
        
def main():
    safe_Vault = Vault() # Create an instance of Vault
    unsafe_Vault = UnsafeVault() # Create an instance of UnsafeVault
    
    input_key = input("Enter the key to unlock the vault: ")
    
    print(safe_Vault.vault_Lock(input_key)) # This will print the secret phrase if the key is correct, otherwise "Access Denied"
    
    print("Unsafe Vault Secret:", unsafe_Vault.secret_Phrase) # This will print the public attribute
    # print("Safe Vault Secret:", safe_Vault.__secret_Phrase)  # This will raise an AttributeError
    # print(safe_Vault.__get_Secret_Phrase())  # This will raise an AttributeError
    
if __name__ == "__main__":
    main()