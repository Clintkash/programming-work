number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):

    if(i % 2 == 0): #We use the % sign for dividing and. this section means that what ever the user inputs that is divisible by 2 without any remender should be prined. if we are to change it to ==1, it will calculate odd numbers.

        y =(i**2) #The **2 is a way of saying squares of a nmuber  the y is a variable given to the squares of the input even numers(numbers divisible by 2 that has 0 as a remender).

        sum +=y # if we rempove the + sign here, the program will just print the square root of the given number
print(sum)
#this program is to print the squares of even numbers of a given number