print(' WELCOME TO ABBYS CLOTHING')
print('**************************************************************************')
print('BELOW ARE THE LIST OF ITEMS WE HAVE IN OUR STORE AND THERE PRICES')
for items in 'POLO=$9.99', 'T-SHIRT=$9.99', 'JEANS=$20', 'SWEAT PANTS=$20':
    print(items)

Type=1
Trousers=1

Type= int(input('please press 1 for polo and 2 for T-shirt: '))

if Type==1:
    print('You have selected a POLO')
elif Type==2:
    print('You have selected a T-shirt')
elif Type !=1 and Type!=2:
     print ('ERROR!!!!!...........please press 1 for polo and 2 for T-shirt.' )

Trousers= int(input('Please press 1 for jeans and 2 for sweat pants: '))

if Trousers==1:
    print('You have selected a Jean')
elif Trousers==2:
    print("You have selected a sweat pant")
elif Trousers!=1 and Trousers!=2:
    print('ERROR!!!...... YOU HAVE TO PRESS 1 OR 2 TO CHOOSE')

colour= str(input('Please type in the colour you want, all colours are available for our shirts.: '))

print('WE ONLY HAVE THREE COLOURS AVAILABE FOR OUR TROUSERS BELOW ARE THE AVAILABLE COLOURS.')
for types in 'BLUE', 'RED', 'WHITE':
    print(types) 

Colour= str(input('PLEASE RED BLUE OR WHITE FOR TROUSER COLOUR.: '))

if Colour== 'RED' or Colour== 'red':
        print('You have selected red colour for your trouser of choice')
elif Colour== 'BLUE' or Colour== 'blue':
        print('You have selected a Blue colour for your trouser of choice')
elif Colour== 'WHITE' or Colour== 'white':
        print('You have selected a white colour for your trouser of choice')
else:
    print(" ERROR!!!.... The colour you selected is not available please try again")

if Type==1:
    print('You have selected a ' +str(colour) + ' POLO')
elif Type==2:
    print('You have selected a ' +str (colour) + ' T-shirt')
elif Trousers==1:
    print('You have selected a ' +str (Colour) + ' jeans')
if Trousers==2:
    print('You have selected a ' +str (Colour) + ' Sweat Pants')

print("WE HAVE A 10% DISCOUNT FOR SENIORS AND STUDENTS, ALSO A 15% DISCOUNT IF YOU PURCHASE 3 OR MORE TROUSERS FROM OUR STORE ONLY ONE OF THE DISCOUNTS APPLY.")
print("To qualify for the discount, answer  the questions below to indicate if you are a student or senior")
discount= str(input("ARE YOU A STUDENT OR SENIOR? TYPE IN 'S' FOR STUDENT AND 'Y' IF YOU ARE A SENIOR OR 'Q' IF U ARE NOT A STUDENT OR SENIOR CITIZEN: "))
if (discount== 'Y') or (discount=='S' ):
    print('YOU ARE  QUALIFIED FOR THE 10% DISCOUNT.')
else:
    print('YOU ARE  NOT QUALIFIED FOR THE 10% DISCOUNT.')

Quantityofshirts= int(input('Please type in the amount of shirts  you will love to purchase: '))
Quantityoftrousers= int(input('Please type in the amount of Trousers you will love to purchase: '))
if Quantityoftrousers>=3:
    print('YOU ARE QUALIFIED FOR A 15% DISCOUNT FOR PURCHASING UP TO THREE(3) TROUSERS IN OUR STORE')
elif Quantityoftrousers<3:
   print('YOU DO NOT QUALIFY FOR THE 15% DISCOUNT')

if Type==1:
    print('You have selected a POLO')
elif Type==2:
    print('You have selected a T-shirt')

if Trousers==1:
    print('You have selected a Jean')
elif Trousers==2:
    print("You have selected a sweat pant")

print('The colour of shirt is ' +str (colour))
print('The colour of trouser is ' +str (Colour))
print('THE SENIOR/STUDENT DISCOUNT ONLY APPLIES FOR THE SHIRTS AND THE 15% DISCOUNT APPLIES ONLY WHEN YOU PURCHASE THREE(3) OR MORE TROUSERS FOR THE TROUSERES ALONE')

priceofshirts= 9.99
subtotal= priceofshirts*(Quantityofshirts)
  
priceofjeans= 20.00
subtotal1=priceofjeans*(Quantityoftrousers)
TOTALPRICE=subtotal+subtotal1

x=TOTALPRICE*0.75
format_x="{:.2f}".format(x)
print('SUBTOTAL IS ' +str (format_x))
HST=0.13*(x)
format_HST="{:.2F}".format(HST)
print('HST IS ' +format_HST)
TOTAL=HST+x
format_TOTAL= "{:.2F}".format(TOTAL)
print('TOTAL IS ' +str (format_TOTAL ))
print("THE 15% QUANTITY DISCOUNT AND 10% DISCOUNT WAS APPLIED AFTER TAX")
print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')