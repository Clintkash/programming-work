print(' WELCOME TO ABBYS CLOTHING')
Type=1

Type= int(input('please press 1 for polo and 2 for T-shirt: '))

if Type==1:

    print('You have selected a polo.')

elif Type==2:
    print('You have selected a T-shirt.')

elif Type!=1  and Type!=2 :
     print ('ERROR!!!!!...........please press 1 for polo and 2 for T-shirt.' )

colour= str(input('Please type in the colour you want, all colours are available: '))


print('All the clothes in our store cost $9.99 each')
Quantity= int(input('Please type in the amount you will love to purchase: '))

#print("The type of shirt you want is a "  +str (Type))
if Type==1:

    print('The type of shirt you want is A polo')

elif Type==2:
    print('The type of shirt you have want is a T-shirt.')

    
print('The colour is ' +str (colour))
print('The quantity you wish to buy is ' +str (Quantity))

price=9.99
#format_price= "{:.2f}".format(price)
subtotal= price*(Quantity)
print("The subtotal is " +str (subtotal))


HST= 0.13*(subtotal)
format_HST= "{:.2F}".format(HST) #the '{:.2f}' is used to print the numbers in two decimal places.
print('HST is ' +format_HST)

TOTAL=subtotal+ HST
format_TOTAL= "{:.2f}".format(TOTAL)
print("TOTAL is " +str  (format_TOTAL))

print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')


