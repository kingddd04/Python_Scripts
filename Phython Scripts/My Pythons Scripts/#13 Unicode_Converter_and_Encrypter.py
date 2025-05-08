#UNICODE CONVERTER AND ENCRYPTER

def encrypter(nubers_list,encryption_key):
    if len(str(encryption_key)) != 8:
        raise ValueError("Your decryption key must have 8 numbers!")
    key1 = int(encryption_key[:2])
    key2 = int(encryption_key[3:4])
    key3 = int(encryption_key[5:6])
    key4 = int(encryption_key[7:8])
    results = []
    
    for item in nubers_list:
        dec_int = item*key1//key2-key3+key4
        results.append(dec_int)
    
    return results
    
def decrypter(encrypted_numbers_list, decription_key ):
    if len(str(decription_key)) != 8:
        raise ValueError("Your decryption key must have 8 numbers!")
    key1 = int(decription_key[:2])
    key2 = int(decription_key[3:4])
    key3 = int(decription_key[5:6])
    key4 = int(decription_key[7:8])
    res = []
    
    for i in encrypted_numbers_list:
        dec_int = i//key1*key2+key3-key4
        res.append(dec_int)
          
    return res

#def get_int_list(string_list):
    
    
def list_str_to_list(list_str):
    list_string = list_str.strip("[]")

    # Split the string by commas and convert each item to an integer
    list_actual = [int(item) for item in list_string.split(",")]

    return list_actual
        
def converter(Datas, Operation):
    Choose_Operation = None
    if "toint" in Operation:
        Choose_Operation = True
    if "tostr" in Operation:
        Choose_Operation = False
        
    if Choose_Operation == True:
        int_list = []
        for char in Datas:
            int_list.append(ord(char))
        return int_list
    
    if Choose_Operation == False:
        Out_string = ""
        Converted_int_list = list_str_to_list(Datas)
        for n in Converted_int_list:
            Out_string = Out_string+chr(n)
        return Out_string
        
            
            
    
listu = [110, 105, 103, 103, 97]
print(decrypter([332, 317, 311, 311, 293], "12345678"))