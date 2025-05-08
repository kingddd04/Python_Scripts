def remove_extra_spaces(s):
    # Split the string into words
    words = s.split()
    print(words)
    # Join the words back together with one space between each word
    result = ' '.join(words)
    return result

def Value_extractor_from_txt(file_in):
    new_list = []
    with open(file_in,"r",encoding="utf8") as a:
        lines_list = a.readlines()
    for line in lines_list:
        t_line = remove_extra_spaces(line)
        new_list.append(t_line)
    
    return new_list

print(Value_extractor_from_txt("C:/Users/david/OneDrive/Documents/Phython Scripts/My Pythons Scripts/Test Material/text and spaces.txt"))
