#Functions, or methods this is the logical part of the program

def Process_Text(imput_text):
    imput_text = imput_text.replace("'", " ")
    imput_text = imput_text.replace("\n", " ")
    result = ""
    for char in imput_text:
        if char == " ":
            result += char
        if char.isalpha():
            result += char
    return result

def conta_occorrenze_parole(imput_text):
    # Create a dictionary to track occurrences
    occorrenze = {}

    # Split the text into words
    parole = imput_text.split()

    # Count occurrences of each word
    for parola in parole:
        # Remove punctuation from words
        parola = parola.strip('.,!?')
        if parola.isdigit():  # Exclude digits
            continue
        # Convert to lowercase for case-insensitive counting
        parola = parola.lower()
        if parola in occorrenze:
            occorrenze[parola] += 1
        else:
            occorrenze[parola] = 1
       # Sort the dictionary by values in descending order
    print("\n---RESULTS : ---\n")
    sorted_occorrenze = dict(sorted(occorrenze.items(), key=lambda item: item[1], reverse=True))
    
    for word, count in sorted_occorrenze.items():
        print(f"{word}: {count}")


    return  sorted_occorrenze

#Here we have thing that in java is called main the part of the program that executes instructions in order

#Presentation
print("\nWord Occurrences counter 3000:\n\nSelect the text that you want to be scanned!\n\n1 = select text from file\n2 = select text from prompt\n\n")
Command_Select = input("-Select your action : ")

#Program menù
# Extract test from file 
if "1" in Command_Select:
    PathSelector = input("\nImsert your filepath now ... .")
    if "\"" in PathSelector:
        PathSelector=PathSelector[1:-1]
    with open(PathSelector, "r", encoding="utf-8") as text:
        text_datas = text.read()
    imput_text = Process_Text(text_datas)
    conta_occorrenze_parole(imput_text)
#Exrtract test from user console imput
elif "2" in Command_Select:
    text_datas = input("\nInsert your text here ... \n") 
    imput_text = Process_Text(text_datas)
    conta_occorrenze_parole(imput_text)
else:
    print("Wrong imput try again!")
