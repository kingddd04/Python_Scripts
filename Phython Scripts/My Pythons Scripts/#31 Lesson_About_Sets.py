numbers_list = [0,1,2,3,4,5,6,7,8,9,10,3,4,2,1,4,100,777,2,9]
numbers_unique = set(numbers_list)
letters_unique = {"a","b","c","d","e","f","u"}
numbers_unique_2= {1,23,2,511,33,44,77,99,144,3}

print("""
      - - - - - - -Sets Lessons in Python- - - - - - - - - - - - - - - -
      
      -So basically sets in python are are a type of data structure similar
      to lists but with no repetition
      
      - Sets are a lot more efficient than lists for finding items because
      are stored in a random order with no duplicates and because of this
      are stored in a hash table wich is faster to scan
      
      A Set can be created from a list using set function, the set function
      is the only way to create a empty set giving no arguments to it like this set()
      
     """)
print("-List = "+str(numbers_list)+"\n-Set = "+ str(numbers_unique))

print(""" 
      - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
     
      -We can add and remove things if we wish to do so using:
        Myset.add(item) 
        Myset.remove(item)
        
     -We can also add multiple items using the update function
         - Myset.update(mylist)  // -Myset.update(Myset2)
         
     -We can remove multiple items using also discard(items)
         -Myset.discard(value)
     
     -Also we can use len to know how many variables the set contain
         lenset = len(set)
         
    -Unlike lists indexing dosen't work on sets so you must convert to list your
    data structure using list(myset) however the "if in myset" method works also in sets
    so you can use them
    
    """)
letters_unique.add("z")
print("\t-Set length = " +str(len(numbers_unique)))

print(""" 
      - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
      
      -We can do the union of two sets typhing "Set1 | Set2"
          this operation returns the variables in both sets without repetition
          
      -We can intersect two sets using "Set1 & Set2"
          this operation returns the variables in common between the two sets
          
      -We can do the difference of the two sets doing "Set1 - Set2"
          this operation return the variables not in the first set but
          not in the second if you wanna do the opposite comparison
          just invert Set2 and Set1

Examples:
    """)
print(numbers_unique)
print(numbers_unique_2)
print("")
print("\t- Union  | : "+ str(numbers_unique | numbers_unique_2))
print("\t- Intersection  & : "+ str(numbers_unique & numbers_unique_2))
print("\t- Difference - : "+ str(numbers_unique - numbers_unique_2))
print("\t- Inverted Difference - : "+ str(numbers_unique_2 - numbers_unique))
    

         
          
      
      
      
    


