import random
import time


"""   Implementation for a single row

row_lenght = random.randint(2,5)
row_cooldown = random.randint(3,4)

for _ in range(0,60):
    time.sleep(0.5)
    if row_lenght == 0:
        if row_cooldown == 0:
            row_lenght = random.randint(2,5)
            row_cooldown = random.randint(3,4)
        row_cooldown -=1 
        print(" ")
    else:
        row_lenght -= 1
        random_number = random.randint(0,7000)
        print(chr(random_number))



columns_lenght = [0,0,0,0]
columns_cooldown = [0,0,0,0]

for _ in range(0,60):
    time.sleep(0,5)


"""

#print(chr(random.randint(0,2663)))

def printColumns(valuelist):
    row = valuelist[0]+"\t\t"+valuelist[1]+"\t\t"+valuelist[2]+"\t\t"+valuelist[3]+"\t\t"+valuelist[4]+"\t\t"+valuelist[5]+"\t\t"+valuelist[6]+"\t\t"+valuelist[7]
    green_row = "\033[32m"+row
    print(green_row)
    
def randomCooldown():
    cooldown = random.randint(4,27)
    return cooldown

def randomLenght():
    lenght = random.randint(3,33)
    return lenght
    


def FallingGreenNumbersPrinter():
    #columns_len = [randomLenght(),randomLenght(),randomLenght(),randomLenght(),randomLenght(),randomLenght()]
    #columns_cooldown = [randomCooldown(),randomCooldown(),randomCooldown(),randomCooldown(),randomCooldown(),randomCooldown()]
    
    

    columns_len = [0,0,0,0,0,0,0,0]
    columns_cooldown = [0,0,0,0,0,0,0,0]
    
    columns_content = [" ", " ", " ", " "," "," "," ", " "]


    for _ in range(0,360):
        time.sleep(0.5)
        for index in range(len(columns_content)):
            if columns_len[index] == 0:
                if columns_cooldown[index] == 0:
                    columns_len[index] = randomLenght()
                    columns_cooldown[index] = randomCooldown()
                columns_cooldown[index] -= 1
                columns_content[index] = " "
            else:
                columns_len[index]-= 1
                columns_content[index] = chr(random.randint(0,1000))
        printColumns(columns_content)
        
        
FallingGreenNumbersPrinter()