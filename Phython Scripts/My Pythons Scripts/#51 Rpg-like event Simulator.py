# -*- coding: utf-8 -*-
"""

Human Event Simulator 
@Autore: Davide

"""

import os


# Classe che crea una persona sul quale verranno testati gli eventi
class Persona:
    def __init__(self, Nome, Età, Intelligenza_Analitica, Intelligenza_Astratta, Fisico, Carisma, Umore, Salute_Mentale, Salute_Fisica):
        self.Nome = Nome
        self.Età = Età
        self.Intelligenza_Analitica = Intelligenza_Analitica
        self.Intelligenza_Astratta = Intelligenza_Astratta
        self.Fisico = Fisico
        self.Carisma = Carisma
        self.Umore = Umore
        self.Salute_Mentale = Salute_Mentale
        self.Salute_Fisica = Salute_Fisica
        
    #Metodo che stampa gli attributi dell ogetto persona
    def Stampa_Attributi(self):
        print("\tPersona\n")
        print("Nome:", self.Nome, "Età:", self.Età) 
        print("Intelligenza Analitica:", self.Intelligenza_Analitica, "Intelligenza Astratta:", self.Intelligenza_Astratta)
        print("Fisico:", self.Fisico, "Carisma:", self.Carisma, "Umore:", self.Umore)
        print("Salute Mentale:", self.Salute_Mentale, "Salute Fisica:", self.Salute_Fisica)
        
# Questa funzione crea un ogetto persona a partire dai dati presenti all'interno di una cartella test material separati da virgole
def Crea_Persona_From_File():
    cwd = os.getcwd()
    fullpath = cwd + "/"+ "Test Material"+ "/"+ "Persona.txt"
    with open(fullpath, "r", encoding="utf8") as datas:
        text = datas.read()    
    Attributes = text.split(",")
    for n_element in range(len(Attributes)):
        if Attributes[n_element].isdigit():
            Attributes[n_element] = int(Attributes[n_element])
            
    return Persona(Attributes[0], Attributes[1], Attributes[2], Attributes[3], Attributes[4], Attributes[5], Attributes[6], Attributes[7], Attributes[8])

# Questa funzione calcola data una lista di skills la media dei valori tra queste 
def Total_skill_power_Calc(Skill_List):
    res_t = 0
    for skill in Skill_List:
        temp = getattr(persona_1, skill)  # Ottiene il valore corrente dell'attributo chiamato skill
        #print(type(temp))
        res_t += temp
    res = res_t // len(Skill_List)
    return res

# Questa funzione premde in imput una lita delle skills da aggiornare e dei valori con il quale aggiornarle
def Victory_Prize(Skills_To_Update, Values_to_Update_List):
    for n in range(len(Skills_To_Update)):
        current_value = getattr(persona_1, Skills_To_Update[n])  # Ottiene il valore corrente dell'attributo chiamato skill to update
        setattr(persona_1, Skills_To_Update[n], current_value+ Values_to_Update_List[n]) # Rimpiazza il valore dell'attributo chiamato Skills_To_Update con  current value + l'altra roba
    return
    
    
    
# Questa funzione premde in imput una lita delle skills da aggiornare e dei valori con il quale aggiornarle in negativo in caso di sconfitta.
def Defeat_punishment(Skills_To_Update, Values_to_Update_List):
    for n in range(len(Skills_To_Update)):
        current_value = getattr(persona_1, Skills_To_Update[n])  # Ottiene il valore corrente dell'attributo chiamato skill to update
        setattr(persona_1, Skills_To_Update[n], current_value+ Values_to_Update_List[n]) # Rimpiazza il valore dell'attributo chiamato Skills_To_Update con  current value + l'altra roba
    return
    

# Funzione per stampare il risultato dell'evento
def Print_Event(event_nam, event_des, esit_mess, skill_To_Update, skill_bonus_n, Victory):
    sign = "+"
    if Victory == False:
        sign = "-"
    print("\n--Nuovo Evento--")
    print("\n\tNome Evento:", event_nam)
    print("\n\tDescrizione Evento:", event_des)
    print("\n\tEsito:", esit_mess)
    print("\n\t--Risultati--\n")
    for n in range(len(skill_To_Update)):
        print("\t\t"+skill_To_Update[n] + sign + str(skill_bonus_n[n]))
    return

    
    
    
# Applica eventi basati su dati letti da un file di testo e aggiorna l'oggetto Persona di conseguenza
def Applica_evento():
    cwd = os.getcwd()
    fullpath = cwd + "/"+ "Test Material"+ "/"+ "Eventi.txt"
    with open(fullpath, "r", encoding="utf8") as datas:
        text_lines = datas.readlines()
    for event in text_lines:
        event_details = event.split(",")
        event_name = event_details[0]
        event_req_skills = [skill for skill in event_details[1].split()]
        required_skill_score =  int(event_details[2])
        event_bonus_skills = [bskill for bskill in event_details[3].split()]
        event_bonus_n = [int(bn) for bn in event_details[4].split()]
        event_defeat_skills = [dskill for dskill in event_details[5].split()]
        event_defeat_n = [int(bn) for bn in event_details[6].split()]
        b_message = event_details[7]
        d_message = event_details[8]
        event_description = event_details[9]
        
        skills_res = Total_skill_power_Calc(event_req_skills)
        if skills_res >= required_skill_score:
            Victory_Prize(event_bonus_skills, event_bonus_n)
            Print_Event(event_name, event_description, b_message, event_bonus_skills, event_bonus_n, True)
        else:
            Defeat_punishment(event_defeat_skills, event_defeat_n)
            Print_Event(event_name, event_description, d_message, event_defeat_skills, event_defeat_n, False)
    return 

# Chiamate    

persona_1 = Crea_Persona_From_File()
persona_1.Stampa_Attributi()
Applica_evento()

        