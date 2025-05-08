# -*- coding: utf-8 -*-


import images

def jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
    
    def Tile_Rotator(Puzzle_Tile):
     
    
    Puzzle= images.load(puzzle_image)
    Puzzle_Tile=[]
    Expected_Image=images.load(plain_image)
    Expected_Tile=[]
    key=""
    rotated_tile=[]
    num_tile_y= len(Puzzle) //tile_size #altezza
    num_tile_x= len(Puzzle[0]) //tile_size  #larghezza
    start_pix=0
    end_pix=tile_size
    Keep_Alive= True
    Keep_Alive1= True
    Rotation_Num=0
    height, width = len(Puzzle),len(Puzzle[0])


    while Keep_Alive == True:
        
        for line in Puzzle[start_pix:end_pix]:
            Puzzle_Tile.append(line[start_pix:end_pix])
         
        for line in Expected_Image[start_pix:end_pix]:
            Expected_Tile.append(line[start_pix:end_pix])
        print(Expected_Tile)
        if Puzzle_Tile==Expected_Tile:
            key=key+""
        if Puzzle_Tile!=Expected_Tile:

            
        start_pix= start_pix+tile_size
        end_pix=tile_size+tile_size
        
        
if __name__ == '__main__':
    print(jigsaw('tests/test01_in.png', 'tests/test01_exp.png', 20,
                                    'tests/test01_enc.txt', 'output/test01_out.txt'))