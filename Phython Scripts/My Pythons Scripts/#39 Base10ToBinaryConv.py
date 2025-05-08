#timeit 

print("""      
      Binary Number Converter 1.0
      
          -Instructions:
              1-Select operation Type:
                  -ToBin To convert From base 10 to Binary
                  -To10 To convert from binary to base 10
             2-Insert Numbers      
             
      """)

def  Input_Check(str_input,Operation_Type):
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    if Operation_Type == True:
        for l in str_input:
            if l != "0" and l != "1":
                raise ValueError("This converion can accept only 0 and 1")  
    if Operation_Type == False:
        for l in str_input:
               if l not in numbers:
                  raise ValueError("Only Numbers Are Allowed")
        

def Base10toBinary(str_input):
    Input_Check(str_input,False)
    int_to_convert = int(str_input)
    res = ""
    while int_to_convert != 0 :
        if int_to_convert % 2 == 0:
            res+= "0"
        else:
            res+= "1"
        int_to_convert = int_to_convert // 2
    res = res[::-1]
    return res
        
def BinarytoBase10(str_input):
    Input_Check(str_input,True)
    exp = 0
    res = 0
    for i in range(len(str_input)):
        temp = pow(2, exp)
        temp2 = temp * int(str_input[i])
        res += temp2
        exp +=1
    return res
        
OP_t = input("-Select operation type - ")
if OP_t == "tobin":
    str_input = input("\n-Insert Your Number Here!   ... ")
    print("\n-- Output --\n")
    print(Base10toBinary(str_input))
elif OP_t =="to10":
    str_input = input("\n-Insert Your Number Here!   ... ")
    print("\n-- Output --\n")
    print(BinarytoBase10(str_input))
                