number = int(input("Enter a number: "))
sum = 0
for i in range(1, number + 1):

    if(i % 2 == 1):
        y =(i**2)
        
        sum +=y
print(sum)