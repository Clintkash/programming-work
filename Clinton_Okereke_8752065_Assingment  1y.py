print('WELCOME TO ABBYS MERCHANDZING STORE. HERE WE SELL MANY QUALITY POLOS AND T-SHIRT ')
Type= str(input('please type in the type of Shirt you want, we have the POLO and T-SHIRT.'))

Colour= str(input('Please type in the colour you want all colours are available.'))

print ("Each T-shirt and polo in our store cost $9.99")  

print("Please enter the quantity you will wish to buy.")
quantity= int(input())

print("The type of shirt you want is A " +str (Type))
print('The colour is ' +str (Colour))
print('The quantity you wish to buy is ' +str (quantity))

price=9.99
subtotal= price*(quantity)
print("The subtotal is " +str (subtotal))


HST= 0.13*(subtotal)
print('HST is ' +str (HST))


TOTAL=subtotal+ HST
print("TOTAL is " +str (TOTAL))

print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')
