print('THIS IS A MINI CALCULATOR THAT DOES SOME BASIC CALCULATIONS LIKE ADDITION, SUBTRACTION, MULTIPLICATION, DIVISION AND MODULUS DIVISION OF NUMBERS.')
print("***********************************************")
print('BELOW ARE THE LIST OF OPERATIONS YOU CAN DO PRESS THE FOLLOWING NUMBERS TO PERFORM ANY OPERATION OF YOUR CHOICE.')
for operations in 'FOR ADDITION, PRESS 1', 'FOR SUBTRACTION, PRESS 2', 'FOR MULTIPLICATION, PRESS 3', 'FOR DIVISION, PRESS 4', 'FOR MODULUS DIVISION,PRESS 5':
    print(operations)

def addition():
    x=int(input('Enter your first number: '))
    y=int(input('Enter your second number: '))
    print(x+y)

def subtraction():
    x=int(input('Enter your first number: '))
    y=int(input('Enter your second number: '))
    print(x-y)

def division():
    x=int(input('Enter your first number: '))
    y=int(input('Enter your second number: '))
    print(x/y)

def multiplication():
    x=int(input('Enter your first number: '))
    y=int(input('Enter your second number: '))
    print(x*y)

def modulus_division():
    x=int(input('Enter your first number: '))
    y=int(input('Enter your second number: '))
    print(x%y)

a=int(input('INPUT THE NUMBER YOU WANT BASED ON THE OPERATION YOU WISH TO PERFORM: '))
if a==1:
    addition()
elif a==2:
    subtraction()
elif a==3:
    multiplication()
elif a==4:
   division()
elif a==5:
    modulus_division()
else:
    print('ERROR!!!!!!! You have entred a wrong operation.....')
print("THANK YOU FOR USING CLINT'S CALCULATOR :) ")
