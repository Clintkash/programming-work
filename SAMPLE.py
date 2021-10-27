

from Clinton_Okereke_8752065_Assignment2 import Quantityoftrousers


if Quantityoftrousers>=3:
    y=TOTALPRICE*0.85
    format_y="{:.2f}".format(y)
    print("SUBTOTAL IS " +str (format_y))
HST=0.13*y
format_HST='{:.2f}'.format(HST)
#print("HST IS " +format_HST)
TOTAL=HST+y
format_TOTAL="{:.2F}".format(TOTAL)

print('TOTAL IS ' +str (format_TOTAL))
print('15% DISCOUNT WAS APPLIED BEFORE TAX BECAUSE YOU PURCHASED MORE THAN ONE TROUSER')
print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')




if (discount== 'S') or (discount== 'Y'):
    z=TOTALPRICE*0.9
    print("SUBTOTAL IS " +str (z))
HST=0.13*z
format_HST='{:.2f}'.format(HST)
print("HST IS " +format_HST)
TOTAL=HST+z
format_TOTAL="{:.2F}".format(TOTAL)
print('TOTAL IS ' +str (format_TOTAL))
print('10% DISCOUNT WAS APPLIED BEFORE TAX')
print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')



priceofjeans= 20.00
subtotal1=priceofjeans*(Quantityoftrousers)
TOTALPRICE=subtotal+subtotal1

while Quantityoftrousers>3 and (discount!= 'Y'or 'y') or (discount!='S' or 's'): 
    TOTALPRICE= subtotal1+subtotal
    break
formart_TOTALPRICE="{:.2F}".format(TOTALPRICE)
print('SUBTOTAL IS ' +str (formart_TOTALPRICE))
HST=0.13*(TOTALPRICE)
format_HST="{:.2F}".format(HST)
print('HST IS ' +format_HST)
TOTAL=HST+TOTALPRICE
format_TOTAL= "{:.2F}".format(TOTAL)
print('TOTAL IS ' +str (format_TOTAL))
print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')




def discount15 (quantityoftrousers):
    discount= 0.85
    price= 29.99
    total= price*quantityoftrousers
    total1= total*discount
    total2=total1*0.13
    return total2
a=int(input("please enter the quantity: "))
d=int(input("please enter quantity of shirt"))
c=a+d*0.13
format_c="{:.2f}".format(d)
print(discount15(c) +str(format_c))

def discount10(quantityoftrousers):
    discount1=0.9
    price=29.99
    total=price*quantityoftrousers
    total1=total*discount1
    total2=total1*0.13
    return total2
b=int(input('please enter quantity: '))
c=int(input('please enter quantity of shirt: '))
d=b+c*0.13
format_d="{:.2f}".format(d)
print(discount10(d) +str(format_d))

def nodiscount(quantityoftrouser):
    price=29.99
    total=price+quantityoftrouser
    total1=total*0.13
    return total1
x=Quantityoftrousers
y=int(input('please input quantity of shirt'))
k=x+y*0.13
format_k="{:.2f}".format(k)
print(nodiscount(d) +str(format_k))