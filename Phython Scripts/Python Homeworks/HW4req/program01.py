import os

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
    source_path = os.path.abspath(source_root) 
    os.makedirs(target_root)
    target_path = os.path.abspath(target_root)
    with open(os.path.join(source_path,"index.txt")) as index:
        readlines = index.readlines()
        Dictionary={}
               
        def song_lenght_calc(source_path, SongFullPath):
            with open(os.path.join(source_path, SongFullPath)) as file:
                SongText = file.read()
                SongLenght=0
                for char in SongText:
                    if char.isdigit():
                        SongLenght += 1
                    elif char.isspace() and char != "\n":
                        SongLenght += 1
                return SongLenght 
            
        def UpgradeIndex(source_path, SongFullPath):
            percorso_cartella = target_path
            percorso_completo = percorso_cartella + "/index.txt"
            dizionario_ordinato = dict(sorted(Dictionary.items(), key=lambda item: (-item[1], item[0])))
            with open(percorso_completo, 'w') as file:
                for chiave, valore in dizionario_ordinato.items():
                    file.write(f" \"{chiave}\" {valore}\n")
                    
        def Translate(SongFullPath):
            with open(os.path.join(source_path,SongFullPath)) as file:
                Text="" 
                for line in file:
                    Text= Text+line[::-1]
            Text = Text.translate(str.maketrans('0123456+- ','ABCDEFG#bP'))    
            current_char = Text[0]
            char_count = 1
            song_length = 0
            i = 1    
            length = 1
            return_text = ""
            while Text[i] not in '\n':
                
                if Text[i:i+length] == current_char and Text[i+length] not in '#b':
                    char_count += 1
                    i += length
                
                elif Text[i] in '#b':
                    current_char += Text[i]
                    length = 2
                    i += 1
                
                else:
                    return_text += current_char + str(char_count) 
                    song_length += char_count
                    current_char = Text[i]
                    char_count = 1
                    i += 1
                    length = 1
                
            song_length += char_count
            return_text += current_char + str(char_count) + '\n'

            return return_text
            
                    
        def TranslateSave(TitleText, SongFullPath):
            Filepath= target_root + "/" + SongFullPath
            Filepath1=os.path.dirname(Filepath)
            os.makedirs(Filepath1, exist_ok=True)
            Filepath2= Filepath1 + "/" + TitleText +".txt"
            with open(Filepath2, 'w') as file:
                file.write(Translate(SongFullPath))
            
                         
            
            
        for line in readlines:
            TextLine = line.split("\" \"")
            TitleText=TextLine[0][1:]
            SongFullPath = TextLine[1][:-2]
            Song_Lenght=song_lenght_calc(source_path, SongFullPath)
            Dictionary[TitleText] = Song_Lenght
            print(TranslateSave(TitleText, SongFullPath))  
                                            
    print(Dictionary)
    print(UpgradeIndex(TitleText,Song_Lenght))
    return Dictionary
