# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 10:22:01 2024

@author: david
"""
def list_comparer(list_a, list_b):
    result = [] 
    for obj in list_a:
        if obj in list_b:
            result.append(obj)
    print(result)
    result.sort()
    return result

def dic_comparer(dic1,dic2):
    
    return

def dic_sorter(dic1):
    sorted_dict = dict(sorted(dic1.items(), key=lambda item: item[1]))
    return sorted_dict
    
def list_sorter(l1):
    sorted_list = sorted(l1, key=str.lower)
    return sorted_list


l1 = ["1","2","3","4","5","6","7","8","9","0","11","life","hope","nova","legacy","moon","whisper","alpha","zeta","Apex","Ages"]
l2 = ["1","2","3","4","5","38","28", "92","381","6","7","8","9","life","hope","nova","legacy","moon","whisper","starcruiser","Ages","Ruins","Wind ","Aurora","Apex","zeta","alpha"]
tuple1 = (1,"ciao"),(3,"nova"),(2,"Trekking")
print(dict(tuple1))
print(list_sorter(l1))

