def clean_txt(Raw_Txt):
    Polished_Txt = ""
    for char in Raw_Txt:
        if char.isalpha():
            Polished_Txt += char
    return Polished_Txt

def Equidistant_Letter_Sequences(Polished_Txt, Start_Position, Skip, k):
    ELS_Result = ""
    Txt_Len = len(Polished_Txt)
    current_position = Start_Position
    
    
    while current_position < Txt_Len :
        ELS_Result += Polished_Txt[current_position]
        current_position += Skip
        # Stop when the desired length (k) is reached
        if len(ELS_Result) == k:
            break

    return ELS_Result

def print_result(Result):
    print("       ----Result----")
    print(Result)
    print(" ")
    print("       ----Reversed_Result----")
    print(Result[::-1])
    

print("""---Equidistant_Letter_Sequences_Finder 2.0--
      
     -This tool can help you to find els in a text 
     it is very useful for finding hidden messages!
      
         -Instructions:
             1-Insert your text:
                 -Insert from txt_file(you need the .txt filepath)(type 1)
                 -Insert from console(type 2)
             2-Insert the start position where the search must begin
               (type 0 to do it from the start)
             3-Insert how many letter you want to skip each time
               (no more than the text lenght)(type max for processing all the text)
             4-(Insert how many letter  of the text you want to process)
    
    This tool automatically process the text for making it suitable for els search
    So it will consider for the search only letters and will not consider numbers sybols ecc..      
      """)
Text_insert = input("\nChoose how insert your text (1 from .txt file (2 from console... ")
if "1" in Text_insert:
    txt_filepath = input("\nInsert here your filepath... ")
    with open(txt_filepath,"r", encoding="utf-8") as txt:
        Raw_Txt = txt.read()
if "2" in Text_insert:
    Raw_Txt = input("\nPlease insert here your text or paste it... ")
Polished_Txt = clean_txt(Raw_Txt)
Start_Position = input("\nInsert the start position where the search must begin(only the number)... ")   
Skip = input("\nInsert how many letter you want to skip each time(only the number)... ")
if int(Skip) == 0:
    raise ValueError("Skip can not be 0 !")
k = input("\nInsert how many letter  of the text you want to process... ")
if "max" in k:
    k = str(len(Polished_Txt))
print("\n-Processing...\n")
Polished_Txt = clean_txt(Raw_Txt)
Result = Equidistant_Letter_Sequences(Polished_Txt, int(Start_Position), int(Skip), int(k))
print("-Done!")
print_result(Result)

      



            