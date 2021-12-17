import datetime
class AnalyzeTriangle:
    def __init__(self, input1, input2, input3):
        self.input1=input1
        self.input2= input2
        self.input3= input3

    def validateTriangle(self):
        sum= self.input1+self.input2+self.input3
        if sum == 180:
            print('This is a triangle')
        elif sum != 180:
            print('This is not a Triangle.')
        
    def TriangelType(self):
        both= self.input1!=self.input2
        both1= self.input2==self.input3
        if both1== self.input1:
            print('This is an Equilateral Triangle')
        elif self.input1 != self.input2 and self.input3:
            print("This is a Scalene triangle ")
        elif both!= self.input3:
            print('This is an Isosceles triangle ')


firstnum= int(input('Please enter the first angle of your Triangle: '))
secnum= int(input('Please enter the second angle of your Triangle: '))
thirdnum= int(input('Please enter the third angle of your Triangle: '))

REsult=AnalyzeTriangle(firstnum, secnum,thirdnum)

while REsult.validateTriangle()!=180:
    break
else:
    REsult.TriangelType()


REsult.TriangelType()
x=datetime.datetime.now()

print(x.strftime("THE CURRRENT DATE AND TIME IS: %m/%d/%Y %H:%M:%S"))