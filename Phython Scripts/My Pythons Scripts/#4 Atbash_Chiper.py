#FUnction For the conversion of the text (works in both ways)
def Atbash_Chipher(input_txt):
    #Alphabeth
    Alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #REversed alphabeth
    Inverted_Alphabet = Alphabet[::-1]
    Upper_Alphabet = Alphabet.upper()
    Inverted_Upper_Alphabet = Upper_Alphabet[::-1]
    #Result String
    Converted_Text = ""
    for char in input_txt:
        if char in Alphabet:
            index = Alphabet.find(char)
            Converted_Text = Converted_Text + Inverted_Alphabet[index]
        elif char in Upper_Alphabet:
            index = Upper_Alphabet.find(char)
            Converted_Text = Converted_Text + Inverted_Upper_Alphabet[index]
        else:
            Converted_Text += char

    print("\n-- Here there is the encryption/decryption of your text : "+ Converted_Text+"\n")
    return Converted_Text

# Test dello script
print("""--Atbash Encrypter 1.0--

      Encrypt Your text using the ancient and mighty Atbash Chiper.
      The text translation works in both ways.
      
          Have fun =) 
      
      """)
input_txt = input("Insert the text you want to chiper using Atbash encryption....  ")
Atbash_Chipher(input_txt)
