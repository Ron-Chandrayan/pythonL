#Create a fraction class to implement operator overloading for adding subtracting and multiplying two fractions

class fraction:
    def __init__(self,numerator,denominator):
        if denominator==0:
            raise ValueError("denominator cannot be zero")
        self.numerator=numerator
        self.denominator=denominator
    
    def __add__(self,other):
        num = (self.numerator*other.denominator)+(other.numerator*self.denominator)
        dem = (self.denominator)*(other.denominator)
        return fraction(num,dem)
    
    def __sub__(self,other):
        num = (self.numerator*other.denominator)-(other.numerator*self.denominator)
        dem = (self.denominator)*(other.denominator)
        return fraction(num,dem)
    
    def __mul__(self,other):
        num = self.numerator * self.numerator
        dem = self.denominator * other.denominator
        return fraction(num,dem)
    

f1 = fraction(1,2)
f2 = fraction(3,4)

f3=f1+f2
print(f"{f3.numerator}/{f3.denominator}")
f3=f1-f2
print(f"{f3.numerator}/{f3.denominator}")
f3=f1*f2
print(f"{f3.numerator}/{f3.denominator}")