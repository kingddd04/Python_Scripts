# utf8
def Messages_Printer(message_id):
    if message_id == 0:
        print("""
        Welcome to Python Sea Battle v1.0
        
        -----------------------------------------------
        |                                              |
        |  Instructions:                               |
        |   - Type 'newgame' to start a new game.      |
        |   - Type 'loadgame' to load a saved game.    |
        |     (The file 'SeaBattleSave.txt' must be    |
        |      located in the current directory).      |
        |                                              |
        |  Set Up a New Game:                          |
        |   1. Place Player 1 ships by typing          |
        |      coordinates y and x.                    |
        |   2. Place Player 2 ships in the same way.   |
        |                                              |
        |  Saving the Game:                            |
        |   - Each two turns the game automatically    |
        |     save the game any existing save file     |
        |     will be overwritten.                     |
        |                                              |
        |  Have fun!                                   |
        |                                              |
        -----------------------------------------------
        
        Now choose to start a new game or load a saved one!
       
        """)
    elif message_id == 1:
        print("""
              Insert X coordinates of the ship(between 0 and 9)
              """)
    elif message_id == 2:
        print("""
              Insert Y coordinates of the ship(between 0 and 9)
              """)
    elif message_id == 3:
        print("""
           Insert the Orientation of the ship use "vert" or "oriz" for vertical or orizontal
           """)
    elif message_id == 4:
        print("""
            #Error! You have not inserted valid numbers that can be used for calculations,try again!
              """)
    elif message_id == 5:
        print("""
            #Error! You can only insert "vert" or "oriz" to rotate ships!
              """)
    elif message_id == 6:
        print("""
            # Error! The X coordinates are out of the allowed game board, try again!
              """)
    elif message_id == 7:
        print("""
            # Error! The Y coordinates are out of the allowed game board, try again!
              """)
    elif message_id == 8:
        print("""
            # Error! The Ship cannot overly another existing ship, try again!
              """)
    elif message_id == 9:
        print("""
              Error! Use a supported command!
              """)
    elif message_id == 10:
        print("""
              Player 1's turn. Let's go!
              """)
    elif message_id == 11:
        print("""
              Player 2's turn. Your move!
              """)
    elif message_id == 12:
        print("""
-----------------Success: The game has been loaded successfully!-----------------
              """)
    elif message_id == 13:
        print("""
              Insert X coordinates of the square to attack(between 0 and 9)
              """)
    elif message_id == 14:
        print("""
              Insert Y coordinates of the square to attack(between 0 and 9)
              """)
    elif message_id == 15:
        print("""
              Player 1 Has Won!
              """)
    elif message_id == 16:
        print("""
             Player 2 Has Won!
              """)
    elif message_id == 17:
        print("""
              ----Now is player 1 Turn To Place Ships----
              """)
    elif message_id == 18:
        print("""
              ----Now is pLayer 2 Turn To Place Ships----
          """)
    elif message_id == 19:
        print("""
              ----Now is player 1 Turn Attack----
              """)
              
    elif message_id == 20:
        print("""
              ----Now is player 2 Turn Attack----
              """)
    elif message_id == 21:
        print("""
-----------------Now The Game Can Finally Begin-----------------
          """)
    elif message_id == 22:
        print("""
             Enemy Hit! You have earned an extra Turn!
          """)
          
    
# This function return the list of all the ships
def Ship_list_Creator():
    ship_list = ["°","#","{}", "[]"]
    return ship_list
    

# This function create the game board
def Board_Creator():
    #current_folder = os.getcwd()
    #Save_Game_Filepath = current_folder + "\\" + "Sea_Battle_py.json"
    seaBoard =         [[("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")],
                        [("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~"),("~")]]    
    
    Write_Matrix_Savefile(seaBoard, seaBoard)
    
    Messages_Printer(17)
    board_setup(1)
    Messages_Printer(18)
    board_setup(2)
    
    return
    
# This function returns the length of a ship based on the ship's type represented by a string.
# Why is this approach used?
# - It's more efficient and avoids the need to pass a bulky dictionary to various functions.
# - Simplifies function calls by reducing the number of arguments needed.
# - Minimizes the risk of errors and keeps the code organized.
# Overall, this strategy is more streamlined and less prone to mistakes.

def Get_Ship_len(ship_type):
    if ship_type == "°":
        return 1 
    elif ship_type == "#":
        return 2 
    elif ship_type == "{}":
        return 3 
    elif ship_type == "[]":
        return 4
    else:
        return 0  # Default case if an invalid ship type is provided

# This Program Memory are all saved in a savefile created in loco
# This Script memorizes the players boards in two matrixs separated by "---"
# Each time we want to do an operation we call one of the two functions 
# Write_Matrix_Savefile and Extract_Matrix
# This Metod is very compact and in some way resembles the object oriented programming


# This function writes two matrices (game boards) to a file named "SeaBattleSave.txt".
# The file will contain the first matrix followed by a separator line "---" and then the second matrix.

def Write_Matrix_Savefile(Matrix1, Matrix2):
    # Open the file "SeaBattleSave.txt" in write mode. This will overwrite the file if it already exists.
    with open("SeaBattleSave.txt", 'w') as file:
        # Iterate through each row of the first matrix
        for row in Matrix1:
            # Join the elements of the row with a space and write to the file
            file.write(' '.join(row) + '\n')
        # Write a separator line to distinguish between the two matrices
        file.write("---\n")
        # Iterate through each row of the second matrix
        for row in Matrix2:
            # Join the elements of the row with a space and write to the file
            file.write(' '.join(row) + '\n')
    # Return from the function
    return

    
    
# This function extracts two matrices (game boards) from a file named "SeaBattleSave.txt".
# The file contains the first matrix, followed by a separator line "---", and then the second matrix.
# The function returns the requested matrix based on the Player_Board_Req parameter.

def Extract_Matrix(Player_Board_Req):
    Matrix1 = []  # Initialize an empty list for the first matrix
    Matrix2 = []  # Initialize an empty list for the second matrix
    separation_Detected = False  # Flag to detect the separator line

    # Open the file "SeaBattleSave.txt" in read mode
    with open("SeaBattleSave.txt", 'r') as file:
        rows = file.readlines()  # Read all lines of the file

    # Iterate through each row in the file
    for row in rows:
        if row == "---\n":  # Check if the current row is the separator line
            separation_Detected = True  # Set the flag to True
            
        elif not separation_Detected:  # If separator not yet detected, it's part of the first matrix
            Matrix1.append(row.strip().split(' '))  # Strip and split the row, then append to Matrix1
        else:  # If separator has been detected, it's part of the second matrix
            Matrix2.append(row.strip().split(' '))  # Strip and split the row, then append to Matrix2

    # Return the requested matrix based on Player_Board_Req
    if Player_Board_Req == 1:
        return Matrix1
    elif Player_Board_Req == 2:
        return Matrix2

    

# This function checks if the provided coordinates and orientation are valid for placing a ship on the game board.
# It returns True if the placement is valid, otherwise it returns False.

def Check_Coords(x, y, orientation, ship_type, player_id):
    # Get the length of the ship based on its type
    Ship_Length = Get_Ship_len(ship_type)
    
    # Check if x and y coordinates are digits
    if not (x.isdigit() and y.isdigit()):
        Messages_Printer(4)  # Print error message for invalid coordinates
        return False
    
    # Check if the orientation is either "vert" or "oriz"
    if orientation != "vert" and orientation != "oriz":
        Messages_Printer(5)  # Print error message for invalid orientation
        return False
    
    # Convert x and y to integers
    x, y = int(x), int(y)
    
    # Check if the ship fits within the vertical bounds of the game board
    if orientation == "vert":
        if Ship_Length + y > 10:  # Ensure ship fits within the 10x10 grid
            Messages_Printer(7)  # Print error message for out-of-bounds Y coordinate
            return False
        
    # Check if the ship fits within the horizontal bounds of the game board
    if orientation == "oriz":
        if Ship_Length + x > 10:  # Ensure ship fits within the 10x10 grid
            Messages_Printer(6)  # Print error message for out-of-bounds X coordinate
            return False 
    
    # Extract the current player's seaboard (game board)
    Player_seaboard = Extract_Matrix(player_id)
    
    # Check if the ship can be placed horizontally without overlapping another ship
    if orientation == "oriz":
        for coord in range(x, x + Ship_Length):
            if Player_seaboard[y][coord] != "~":
                Messages_Printer(8)  # Print error message for overlapping ship
                return False

    # Check if the ship can be placed vertically without overlapping another ship
    if orientation == "vert":
        for coord in range(y, y + Ship_Length):
            if Player_seaboard[coord][x] != "~":
                Messages_Printer(8)  # Print error message for overlapping ship
                return False
            
    return True  # If all checks pass, return True indicating valid placement

    
    
    
        
    
    
def Place_Ship(x,y, orientation, ship_type, player_id):
    Player_Board_Matrix = Extract_Matrix(player_id)
    Ship_Lenght = Get_Ship_len(ship_type)
    if orientation == "oriz":
        for coord in range(x,x+Ship_Lenght):
            Player_Board_Matrix[y][coord] = ship_type

    if orientation == "vert":
        for coord in range(y,y+Ship_Lenght):
            Player_Board_Matrix[coord][x] = ship_type
    
    if player_id == 1 :
        Other_Player_Board_Matrix = Extract_Matrix(2)
        Write_Matrix_Savefile(Player_Board_Matrix, Other_Player_Board_Matrix)
            
    if player_id == 2 :
        Other_Player_Board_Matrix = Extract_Matrix(1)
        Write_Matrix_Savefile(Other_Player_Board_Matrix, Player_Board_Matrix)
    
    return         

def Check_Hit_Coordinates(x,y):
    if not (x.isdigit() or y.isdigit()):
        Messages_Printer(4)
        return False
    
    if int(x) > 9 or int(y) > 9:
        Messages_Printer(6)
        return False
    
    return True
    
def Game_Manager(player_id):
    #Variabili Necessarie all'inizio di ogni turno
    Valid_Coords = False
    Opposite_Player_Board = None
    Current_Player_Board = Extract_Matrix(player_id)
    
    # Estrazione dal file delle matrici che rappresentano il tanbellone
    if player_id == 1 :
        Opposite_Player_Board = Extract_Matrix(2)
        Messages_Printer(10)
    
    
    elif player_id == 2:
        Messages_Printer(11)
        Opposite_Player_Board = Extract_Matrix(1)
        
    #Attacco alla flotta avversaria
    while Valid_Coords == False:
        Messages_Printer(13)
        x = input("-> ")
        Messages_Printer(14)
        y = input("-> ")
        Valid_Coords = Check_Hit_Coordinates(x, y)
        
        
    x,y = int(x), int(y)
    #Verifica del colpimento
    if Opposite_Player_Board[y][x] != "~" and Opposite_Player_Board[y][x] != "X":
        Opposite_Player_Board[y][x] = "X"
        Messages_Printer(22)
        Game_Manager(player_id)
        return
    Opposite_Player_Board[y][x] = "X"
    
    if player_id == 1:
        Write_Matrix_Savefile(Current_Player_Board, Opposite_Player_Board)
    else:
        Write_Matrix_Savefile(Opposite_Player_Board, Current_Player_Board)
        
    Victory_Archieved = Check_Victory(Opposite_Player_Board)
    
    # Verifica della vittoria
    if Victory_Archieved == True:
        if player_id == 1 :
           Messages_Printer(15)
        if player_id == 2:
            Messages_Printer(16)
        return
    
    # Gestione turno successivo
    if player_id == 1:
        Game_Manager(2)
    else:
        Game_Manager(1)

    
# This function checks if all ships on the opponent's board have been hit.
# It returns True if there are no ships left, indicating a victory.

def Check_Victory(Opposite_Player_Board):
    # Get the list of valid ship representations
    Valid_Ships = Ship_list_Creator()
    
    # Initialize the victory flag to True
    Victory = True
    
    # Iterate through each row in the opponent's board
    for row in Opposite_Player_Board:
        # Iterate through each square in the current row
        for Square in row:
            # Check if the square contains a part of a valid ship
            if Square in Valid_Ships:
                return False  # If a valid ship part is found, return False (no victory yet)
    
    # If no valid ship parts are found, return True indicating a victory
    return Victory

            
                
# This function places the strings
def board_setup(player_id):
    valid_position = False
    ships = Ship_list_Creator()
    for ship_type in ships:
        while valid_position == False:
            Messages_Printer(1)
            x = input("-> ")
            Messages_Printer(2)
            y = input("-> ")
            Messages_Printer(3)
            orientation = input("-> ")
            valid_position = Check_Coords(x,y, orientation, ship_type, player_id)
        valid_position = False
        Place_Ship(int(x),int(y),orientation,ship_type, player_id)
    if player_id == 2:
        Messages_Printer(21)
        Game_Manager(1)
    return
            

            
    
# Menu principale
def Start_Menù():
    Messages_Printer(0)
    c1 = input("-> ")
    if "newgame" in c1 : # nuovo gioco 
        Board_Creator()
    elif "loadgame" in c1: # carica gioco
        Messages_Printer(12)
        Game_Manager(1)
    else: # Altro comando
        Messages_Printer(9)
        Start_Menù()
    
    
Start_Menù()
        




    