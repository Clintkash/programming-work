#HOW TO DEFINE A FUNCTION
def myfirstfunction(): # as part of our funvtion, we must have the "def" keyword, bracket and colon ":" very important
    print("Hello my name is Clinton hahaha!!!") #this is a function that will work only when we call on it.
#this print statement wont work unless its called upon.

myfirstfunction() #now we have called our function, our print statement will work.

y=9
z=5
def myfunction(y,z):
    x= y+z
    print("hello clinton")
    print(x)
    
myfunction(y,z)
#myfunction(y)
#myfunction(z) #here we  used a parameter and while calling our function, we have to input those variables by defining them as an argument

#suppose we want to print the name and age of a user we will do this below. we pass a parameter.

def function(firstname, age):
    print('hello ' + firstname +" i believe you are " + age + " years old") # always remember to bring back the function to its place.

function("Clinton", str  (19))
function("Kelechi", str  (18))


