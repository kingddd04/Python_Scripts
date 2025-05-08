Words_alphabetical_order = []
Keep_Alive = True

print("""---Alphabetical_Words_Sorter---
      
      This tool can help you to Sort in alphabetical order the words you input in the scriptà
      
                                 --enjoy!
      
      """)
while Keep_Alive:
    words_input = input("\nInsert your words here, separated by underscores (_); leave it empty to skip the process: ")
    temp_words = words_input.split("_")
    Words_alphabetical_order.extend(temp_words)
    Words_alphabetical_order.sort()
    Words_lenght_order = Words_alphabetical_order
    Words_lenght_order.sort(key=len, reverse=True)
    print("\n-Sorted Words-\n")
    for word in Words_alphabetical_order:
        print("-"+word)
    print("\nLongest Word, = "+ Words_lenght_order[0]+"\n")
    print("\nShortest Word, = "+ min(Words_lenght_order, key=len) +"\n")
    


"""
Notes:
    -The append() method adds a single element to the end of a list
    -The extend() method adds multiple elements (usually from an iterable like a list or tuple) 
     to the end of a list and this is the better option in this code
    -sort() method sort a list editing the current list, it does not return anithing
      so avoid doing l = l.sort() and works only on list you kan reverse the order of
      the list using l1.sort(reverse = true) by defoult sort order from smal to big
    -sorted() funziona su molti più iterabili rispetto a sort che si usa solo su liste
      questo metodo può essere usato solo per creare nuove variabili non può editare var esistenti
    -key is a parameter  used to specify sorting order can be used to sort complex datas structures
      
"""
