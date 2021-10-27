class cities:
    def __init__(self, name):
        self.name = name
        self.temp = []

    def enterGrades(self):
        for i in range(3):
            m = float(input("Enter the Temperature readings of %s in day %d : "%(self.name,i+1)))
            self.temp.append(m)
            
    def displayGrades(self):
        print(self.name, " received the following temperatures ", self.temp)

    def getAverage(self):
        summation = sum(self.temp)
        average = summation/len(self.temp)
        print("%s obtained an average temperature of : " %str(self.name),round(average , 1))

firstcity = cities("TORONTO")
firstcity.enterGrades()

secondcity = cities("CALGARY")
secondcity.enterGrades()

thirdcity = cities("THUNDERBAY")
thirdcity.enterGrades()


firstcity.displayGrades()
secondcity.displayGrades()
thirdcity.displayGrades()

firstcity.getAverage()
secondcity.getAverage()
thirdcity.getAverage()