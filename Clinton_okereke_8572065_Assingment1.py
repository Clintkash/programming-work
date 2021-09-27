print("This program is to help with the accurate calculation of clothing in addy's merchandzing store.")

Type= str(input('Do you want a polo or a T-shirt? press "1" for a polo and "A" for a T-shirt.'))

if Type .isalpha():
    print("YOU HAVE SELECTED A 'T-SHIRT'. ")
elif Type .isdigit():
    print("YOU HAVE SELECTED A 'POLO'. ")    

Colour= str(input('What colour do you want?, for red colour, press "1" for white colour press "A".'))

if Colour .isalpha():
    print("You have selected a WHITE colour")
elif Colour .isdigit():
    print("You have selected the RED Colour.")    

print("Each T-shirt and polo cost $9.99")    

print("Please enter the quantity you will wish to buy.")
quantity= float(input())

price=9.99
subtotal= price*(quantity)
print("The subtotal is " +str (subtotal))

HST=0.13*(subtotal)
print('HST is ' +str (HST))

TOTAL=subtotal+ HST
print("TOTAL is " +str (TOTAL))




