# wap to implement inheritance and subclasses

class Test:
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

class grade(Test):

    def __init__(self, m1, m2, m3):
        super().__init__(m1, m2, m3)
        self.totalmarks=self.m1+self.m2+self.m3
        self.perc = (self.totalmarks/3)*100

    def display_grade(self):
        if(self.perc>80):
            print('A')
        elif(self.perc>60 and self.perc<79):
            print('B')
        else:
            print('C')

g=grade(89,87,98)

g.display_grade()
