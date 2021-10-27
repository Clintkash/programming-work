Dictionary1 = {"a":1, "b":2, "c":3  } #we use ":" to specifiy a key value to a data.
print("Dictionary: ", Dictionary1["b"]) # do not forget the "[]" when printing 
# in this print section, its gonna print the 2 because we are using "b" to represent 2 using "b".

setone =set() #we will have to give our set a variable first before doing line 6.
setone = {4,5,6,7}
print("set ", setone)

# sets alwasy prints with the brackets, because they are in a  variale.

#ADDING NEW ITEMS TO A DICTIONARY.
#To add a new item to a dictionary, we use the "[]" to add new items. just like what we will do below, we will add new items to our dictionary.
Dictionary1["d"] = 4
Dictionary1["z"] = 26
del Dictionary1["b"]  #we use the "del" to delete an item from a dictionary.

print("dictionary:", Dictionary1) #we just added an item to our already made dictionary. 

setone.add(3) #for set, we have a built in method for it we just need to type our variable and use the "." sign.
print("set: ", setone)
