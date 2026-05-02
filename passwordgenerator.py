class student:
    def __init__(self , name):
        self.name = name 
        self.__marks = 0

    def marksscored(self , marks):
        if marks<0:
            print("invalid marks")

        else:
            self.__marks = marks


    def getmarks(self):
        return self.__marks 


a = student("albert")
a.marksscored(399)



print(f"Name: {a.name}")
print(f"Marks: {a.getmarks()}")






