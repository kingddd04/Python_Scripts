def merge_dictionaries(dict1, dict2):
    Res_Dict = {}
    for key in dict1:
        Res_Dict[key] = dict1[key]
    for item in dict2:
        if item not in Res_Dict:
            Res_Dict[item] = dict2[item]
    return Res_Dict

dict1 = {"tre": 4,"Due": 3,"Cinque":5}
dict2 = {"ses":23,"Duce":31,"Sesso":11,"Due":23}
print(merge_dictionaries(dict1, dict2))
        