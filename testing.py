priceofshirts= 9.99
subtotal= priceofshirts*(Quantityofshirts)
  
priceofjeans= 20.00
subtotal1=priceofjeans*(Quantityoftrousers)
TOTALPRICE=subtotal+subtotal1

if Quantityoftrousers<3 and (discount!= 'Y'or 'y'):
    TOTALPRICE= subtotal1+subtotal
formart_TOTALPRICE="{:.2F}".format(TOTALPRICE)
print('SUBTOTAL IS ' +str (formart_TOTALPRICE))
HST=0.13*(TOTALPRICE)
format_HST="{:.2F}".format(HST)
print('HST IS ' +format_HST)
TOTAL=HST+TOTALPRICE
format_TOTAL= "{:.2F}".format(TOTAL)
print('TOTAL IS ' +str (format_TOTAL))
print('THANK YOU FOR SHOPPING WITH US SEE YOU NEXT TIME.')

if Quantityoftrousers==3 and (discount== 'Y'or 'y'): #and (discount=='S' or 's'):
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

#Quantityoftrousers<3 and (discount!= 'Y'or 'y') or (discount!='S' or 's'):