
import immagini

'''
    Si progetti la funzione es42(fImageIn, fcolori, fImageOut) che
    modifica il colore di q pixel presenti in un imagine  PNG fImageIn  e salva poi l'immagine
    modificata  in un nuovo file PNG FImageOut.
    La funzione inoltre ritorna il numero di pixel dell'immagine i cui colori sono stati modificati.
    I colori da modificare sono specificati dal file di testo fcolori.
    Il file fcolori ha tante righe quanti sono i colori da modificare.
    Ogni riga di fcolori contiene  6 interi a valori tra 0 e 255.
    I primi tre indicano il colore da modificare
    e i secondi tre il nuovo colore
    Ad esempio la presenza eventuale della riga
    0 0 0  255 255 255
    indica che nell'immagine tutti  i pixel di colore nero ( i.e. di colore  (0,0,0)) devono
    assumere colore bianco (i.e. devono assumere colore (255,255,255)).

    NOTA: i colori devono essere sostituiti contemporaneamente
    (e non con una sostituzione alla volta che potrebbe modificare un pixel piu' volte)

    :param fImageIn: nome del file PNG contenente l'immagine da modificare
    :param fcolori: nome del file di testo in cui trovare i colori da modificare
    :param fImageOut: nome del file PNG in cui salvare l'immagine modificata
    :return: numero di pixel modificati
    '''
    
def es42(fImageIn, fcolori, fImageOut):
    count = 0
    color_dic = {}
    with open(fcolori, "r", encoding="utf8") as txt:
         lines = txt.readlines()
    for line in lines:
        local_numbers  = line.split()
        first_tuple  = (int(local_numbers[0]),int(local_numbers[1]),int(local_numbers[2]))
        second_tuple = (int(local_numbers[3]),int(local_numbers[4]),int(local_numbers[5]))
        color_dic[first_tuple] = second_tuple
    Matrix = immagini.load(fImageIn)
    rows_lenght = len(Matrix)
    coluns_num_ = len(Matrix[0])
    for y in range(rows_lenght):
        for x in range(coluns_num_):
            if Matrix[y][x] in color_dic:
                Matrix[y][x] = color_dic[Matrix[y][x]]
                count += 1
    immagini.save(Matrix, fImageOut)
    return count
                
                
    
                
        
        
        

    



