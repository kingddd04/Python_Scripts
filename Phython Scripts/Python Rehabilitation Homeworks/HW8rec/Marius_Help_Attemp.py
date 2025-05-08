import images

def out_col(img_in, bg):    
    out = []
    countX = {}
    countY = {}
    for r in range(len(img_in)):
        if img_in[r][0] != bg and len(set([img_in[r][c] for c in range(len(img_in[0]))])) == 1: 
            if img_in[r][0] not in countY: countY[img_in[r][0]] = [r]
            else: countY[img_in[r][0]].append(r)
    for c in range(len(img_in[0])):
        if img_in[0][c] != bg and len(set([img_in[r][c] for r in range(len(img_in))])) == 1: 
            if img_in[0][c] not in countX: countX[img_in[0][c]] = [c]
            else: countX[img_in[0][c]].append(c)
    
    if len(countX)>0 and len(countY)>0:
        for key in countY:
            if len(countY[key]) == 1:
                r1 = countY[key][0]
        for key in countX:
            if len(countX[key]) == 1:
                c1 = countX[key][0]
                
        #per assicurarmi di avere la croce che divide in 4 l'immagine il programma dovrebbe assicurarsi che la linea sia continua da cima a fondo | NOTA BENE: ancora non è perfetto e l'output non è completamente corretto, dagli te un'occhiata pensando a sto ragionamento e vedi cosa riesci a tirarne fuori
        
        out.append(img_in[r1][c1])
        sub_img = []
        for row in img_in[r1+1:]:
            sub_img.append(row[c1+1:])
        out.extend(out_col(sub_img, bg))
        sub_img = []
        for row in img_in[:r1-1]:
            sub_img.append(row[c1+1:])
        out.extend(out_col(sub_img, bg))
        sub_img = []
        for row in img_in[r1+1:]:
            sub_img.append(row[:c1-1])
        out.extend(out_col(sub_img, bg))
        sub_img = []
        for row in img_in[:r1-1]:
            sub_img.append(row[:c1-1])
        out.extend(out_col(sub_img, bg))
    return list(filter(lambda color: color != [], out))
    
def ex1(input_file,  output_file):
    # write your code here
    img_in = images.load(input_file)
    bg = img_in[0][0]
    img_out = [bg]
    img_out.extend(out_col(img_in, bg))
    img_out = [img_out]
    images.save(img_out, output_file)


if __name__ == '__main__':
    # write your tests here
    print(ex1('medium02.in.png', 'yo.png'))
